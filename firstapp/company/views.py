from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
# from django.views.generic import CreateView
from django.contrib.auth.models import User
from permission.views import PermissionGroupMixin
from django.http import Http404
from .models import Type, Company, Division, Worker
from .forms import CompanyForm

# Create your views here.


class MainCompanyList(PermissionGroupMixin, View):
    permission_required = ['listener', 'admin']

    def get(self, request, pk = 'none'):
        try:
            company = self.activateCompany(request.user.id)
        except:
            company = ''

        # company = self.activateCompany(request.user.id)
        return render(request, 'company/main.html', {"company": company})


    def activateCompany(self, user_id):
        company = Company.objects.all().filter(user_id = user_id)
        print(company)
        return company

class MainCompanyControl(PermissionGroupMixin, View):
    permission_required = ['admin']

    def get(self, request):
        user_id = request.user.id
        form = CompanyForm()
        # initial=[{ 'user_id': request.user.id }]
        return render(request, 'company/company_control.html', {"form": form})


    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            company_search_ogrn_inn = Company.objects.all().filter(inn = form.cleaned_data['inn'], ogrn = form.cleaned_data['ogrn']).values()
            if company_search_ogrn_inn:
                messages.add_message(request, messages.ERROR, 'Организация не сохранена. Организация уже есть в базе данных')
            company = Company(
                        type = form.cleaned_data['type_id'],
                        user = request.user,
                        name = form.cleaned_data['name'],
                        ogrn = form.cleaned_data['ogrn'],
                        inn = form.cleaned_data['inn'],
                        telephon = form.cleaned_data['telephon'],
                        logo = form.cleaned_data['logo'],
                        url = form.cleaned_data['url'],
                        text = form.cleaned_data['text'],)
            company.save()
            return HttpResponseRedirect(reverse('main_company'))
        return render(request, 'company/company_control.html', {"form": form})




class MainWorkerList(PermissionGroupMixin, View):
    """docstring for Wokers."""
    permission_required = ['admin']

    def get(self, request):
        user_id = request.user.id
        form = CompanyForm()
        # initial=[{ 'user_id': request.user.id }]
        return render(request, 'company/company_control.html', {"form": form})
