from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse


from .models import Contact


class ContactView(View):
    

    def get(self, request):
        return render(request, 'contact/index.html', {})