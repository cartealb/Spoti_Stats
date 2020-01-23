from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from spotify import spotify
# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'home/home.html')