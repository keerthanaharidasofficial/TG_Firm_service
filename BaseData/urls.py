from django.urls import path
from .views import *
urlpatterns = [
    path('base-data/create/API',base_dataAPI_create.as_view(),name='basedataAPI-create'),
    path('base-data/create', base_data_create.as_view(), name='basedata-create'),

]