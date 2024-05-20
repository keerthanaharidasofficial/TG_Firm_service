from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from .forms import *
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

class base_dataAPI_create(APIView):
    def post(self,request):
        f = baseDataSerializer(data=request.data)
        if f.is_valid():
            f.save()
            return Response(f.data)
        return Response(f.errors)
    def get(self,request):
        d = BaseDataAPI.objects.all()
        f = baseDataSerializer(d,many=True)
        return Response(f.data)
class base_data_create(generic.CreateView):
    form_class = baseDataForm
    template_name = 'basedata.html'
    success_url = reverse_lazy('basedata-create')