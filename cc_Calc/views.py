from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.views import generic,View
import requests
from django.apps import apps
from django.urls import reverse_lazy
from django.db import connection
from django.core.management import call_command
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
# Create your views here.

bill_of_Entry = 35
customs_inspection = 0
liability = 0
kp_charges = 0


def error_404_view(request, exception):
    return render(request, '404.html')

def get_BaseData_API(request):
    api_url =r"file:///C:/Users/97150/PycharmProjects/django_projects/TG_Service/baseData-response.json"
    response = requests.get(api_url)
    print(response.status_code)
def reset_id(model_name):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT setval(pg_get_serial_sequence('{model_name}', 'id'), 1, false);")
    call_command('sqlsequencereset', model_name)

class staff_loginView(View):  # pp@tgadmin123
    form_class = staff_login
    template_name = 'staff-login.html'
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)

            if form.is_valid():
                uname = form.cleaned_data['username']
                print(uname)
                pw = form.cleaned_data['password']
                print(pw)
                auth_user = authenticate(request, username=uname, password=pw)
                print('auth_user=',auth_user)
                if auth_user is not None:
                    request.session['login_staff']=uname
                    login(request, auth_user)
                    request.session['user'] = uname
                    return redirect('home-page')
                else:

                    return HttpResponse('Login failed...Email or Password is Incorrect')
            else:
                return HttpResponse('Login failed')
class baseView(View):
    def get(self,request):
        return render(request,'base.html')

class indexView(View):
    def get(self,request):
        request.session['login_staff']=None
        return render(request,'index.html')

class homeView(View):
    def get(self,request):
            return render(request,'home.html')

class calc(generic.CreateView):
    form_class = dataEntryForm
    template_name = 'data-entry.html'
    success_url = reverse_lazy('data-entry')


class entryData_display(generic.ListView):
    model = TariffEntry
    template_name = 'entrydata_display.html'
class entrysheet_deleteView(View):
    model = TariffEntry
    def get(self,request):
        self.model.objects.all().delete()
        return HttpResponse('Data Successfully Deleted')
        
            

class tariffsheet_deleteView(View):
    model = TariffData
    def get(self,request,*args,**kwargs):
        self.model.objects.all().delete()
        return HttpResponse('data deleted successfully')
        
class entrysheet_UpdateView(generic.UpdateView):
    model = TariffEntry
    form = dataEntryForm
    fields = '__all__'
    template_name = 'update-entry.html'
    success_url = reverse_lazy('data-entry')
    def post(self,request,pk):
        if request.method=='POST':
            base_data = apps.get_model('BaseData','BaseData')
            b_d = base_data.objects.all()
            t_d = TariffData.objects.get(id=pk)

            t_e = TariffEntry.objects.get(id=pk)
            t_d.customer = t_e.customer = request.POST.get('customer')
            t_e.load_plan = request.POST.get('load_plan')
            t_e.destination = request.POST.get('destination')
            t_e.value = request.POST.get('value')
            t_e.wt = request.POST.get('wt')
            t_e.commodity = request.POST.get('commodity')
            t_e.VAT_claim = request.POST.get('VAT_claim')
            t_e.save()
            for i in b_d:
                print('base data fields =',i)
                if i.destination == t_e.destination:
                    if t_e.load_plan.lower() == 'console':
                        t_d.b_charge = i.console
                        print('base charge = ',t_d.b_charge)
                    else:
                        t_d.b_charge = i.single
                    if int(t_e.wt)>4:
                        ind = int(t_e.wt)-4
                        t_d.add_wt = i.wt * ind
                    else:
                        t_d.add_wt = 0
                else:
                    continue
                if float(t_e.value) >1000000:
                    t_d.add_liability = float(t_e.value)*1.5/100
                    print('value = ',t_e.value,float(t_e.value))
                print('liability = ',t_d.add_liability)
                if t_e.VAT_claim.lower() == 'yes':
                    t_d.cust_inspection = 52
                if t_e.commodity == 'RD':
                    t_d.kp_charge = 138

                t_d.save()
                print(t_d)
                break
            return redirect('http://127.0.0.1:8000/entry-sheet')
        return HttpResponse('error')

class dataEntryView(View):
    form_class = dataEntryForm
    template_name = 'data-entry.html'
    success_url = reverse_lazy('data-entry')
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    def post(self,request):
        if request.method=='POST':
            base_data = apps.get_model('BaseData','BaseData')
            b_d = base_data.objects.all()
            cust = request.POST.get('customer')
            l_p = request.POST.get('load_plan')
            dest = request.POST.get('destination')
            value = request.POST.get('value')
            wt = request.POST.get('wt')
            comm = request.POST.get('commodity')
            vat = request.POST.get('VAT_claim')

            for i in b_d:
                print('base data fields =',i)
                if i.destination == dest:
                    if l_p.lower() == 'console':
                        base_charge = i.console
                        print('base charge = ',base_charge)
                    else:
                        base_charge = i.single
                    if int(wt)>4:
                        ind = int(wt)-4
                        weight = i.wt * ind
                    else:
                        weight = 0
                else:
                    continue
                if float(value) >1000000:
                    global liability
                    liability = float(value)*1.5/100
                print('liability = ',liability)
                if vat.lower() == 'yes':
                    global customs_inspection
                    customs_inspection = 52
                if comm == 'RD':
                    global kp_charges
                    kp_charges = 138
                t = TariffEntry(customer=cust, load_plan=l_p, destination=dest, value=value, wt=wt, commodity=comm,
                                VAT_claim=vat)
                t.save()
                tariff_data = TariffData(customer = cust,b_charge=base_charge,add_wt=weight,add_liability=liability,bill_entry=bill_of_Entry,cust_inspection=customs_inspection
                                         ,kp_charge=kp_charges)
                tariff_data.save()
                print(tariff_data)
                break

            return redirect('http://127.0.0.1:8000/entry-sheet')
        return HttpResponse('error')

class tariffSheet_display(generic.ListView):
    model = TariffData
    template_name = 'tariff-sheet.html'
class tariff_detailView(generic.DetailView):
    model = TariffData
    template_name = 'tariff-sheet.html'

class logutView(View):
    def get(self,request):
        logout(request)
        request.session['user'] = None
        return redirect('index-page')