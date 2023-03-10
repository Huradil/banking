from django.shortcuts import render,get_object_or_404,redirect
from .models import Client,Credit,Account
from django.urls import reverse
from django.views import generic


class Clients(generic.ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients'


class ClientDetail(generic.DetailView):
    model = Client
    context_object_name = 'client'
    template_name = 'client_detail.html'
    pk_url_kwarg = 'client_id'




