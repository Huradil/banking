from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.Clients.as_view(),name='clients'),
    path('client/<int:client_id>/',views.ClientDetail.as_view(),name='client_detail'),
]