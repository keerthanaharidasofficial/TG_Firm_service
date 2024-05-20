from django.urls import path
from .views import *

urlpatterns=[
    path('base-page',baseView.as_view(),name='base-page'),
    path('',indexView.as_view(),name='index-page'),
    path('TG-staff-login',staff_loginView.as_view(),name='staffLogin'),
    path('home-page',login_required(homeView.as_view()),name='home-page'),
    path('api-data',get_BaseData_API),
    path('tariff-calc',calc.as_view(),name='tariff-calc'),
    path('data-entry-form',login_required(dataEntryView.as_view()),name='data-entry'),
    path('entry-sheet',login_required(entryData_display.as_view()),name='entry-data-display'),
    path('tariff-sheet',login_required(tariffSheet_display.as_view()),name='tariff-sheet-display'),
    path('tariff-value/<pk>',login_required(tariff_detailView.as_view()),name='tariff-detail'),

    path('update-entry-form/<pk>',login_required(entrysheet_UpdateView.as_view()),name='entry-update'),

    path('clear-entry-sheet',login_required(entrysheet_deleteView.as_view())),
    path('clear-tariff-sheet',login_required(tariffsheet_deleteView.as_view())),

    path('TG-staff-logout',logutView.as_view(),name='logout'),

]