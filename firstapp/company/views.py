from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
# from django.views.generic.edit import UpdateView
from django.core.files.storage import FileSystemStorage
# from django.views.generic import CreateView
from django.contrib.auth.models import User
from permission.views import PermissionGroupMixin
from django.http import Http404
from .models import Type, Company, Division, Worker
from .forms import CompanyForm
from django.conf import settings


# Create your views here.



class BaseCompany(PermissionGroupMixin, View):
    permission_required = ['admin']

    def getCompanyByIdUser(self, user_id):
        return Company.objects.all().filter(user_id = user_id)

    def getCompanyByActivated(self, user_id, activated):
        return Company.objects.all().filter(user_id = user_id, activated = activated)

    def getCompanyById(self, user_id, id):
        return Company.objects.all().filter(user_id = user_id, id = id).values()

    def upload(self, file, pk = False):
        fs = FileSystemStorage(settings.MEDIA_ROOT + '/company/logo/', '/company/logo/')
        if pk:
            company = Company.objects.get(id = pk)
            img = str(company.logo)
            if img:
                if fs.exists(settings.MEDIA_ROOT + img):
                    fs.delete(settings.MEDIA_ROOT + img)
        name = fs.get_alternative_name('logo', '.jpg')
        filename = fs.save(name, file)
        return fs.url(filename)

class MainCompanyList(BaseCompany):
    permission_required = ['listener', 'admin']

    def get(self, request):
        company = self.getCompanyByIdUser(request.user.id).order_by('id')
        print(request.session['company'])
        return render(request, 'company/main.html', {"company": company})

# Здесь активируем организацию для выбора правильных работников.
class CompanyActivated(BaseCompany):
    def get(self, request, pk):
        company_activate = self.getCompanyById(request.user.id, pk)
        if company_activate:
            company_activated = self.getCompanyByActivated(request.user.id, activated = 1)
            company_activated.update(activated = 0)
            company_activate.update(activated = 1)
        request.session['company'] = pk
        return HttpResponseRedirect(reverse('main_company'))

class MainCompanyCreate(BaseCompany):
    permission_required = ['admin']

    def get(self, request):
        form = CompanyForm()
        return render(request, 'company/company_create.html', {"form": form})


    def post(self, request):
        form = CompanyForm(request.POST, request.FILES)
        print('Перед проверкой формы')
        if form.is_valid():
            print('ппрошли проверку данных формы')
            # if Company.objects.all().filter(inn = form.cleaned_data['inn'], ogrn = form.cleaned_data['ogrn']).exists():
            #     messages.add_message(request, messages.ERROR, 'Организация не сохранена. Организация уже есть в базе данных')
            upload_file_url = self.upload(form.cleaned_data['logo'])
            company = Company(
                        type = form.cleaned_data['type_id'],
                        user = request.user,
                        name = form.cleaned_data['name'],
                        ogrn = form.cleaned_data['ogrn'],
                        inn = form.cleaned_data['inn'],
                        telephon = form.cleaned_data['telephon'],
                        logo = upload_file_url,
                        url = form.cleaned_data['url'],
                        text = form.cleaned_data['text'],)
            company.save()
            return HttpResponseRedirect(reverse('main_company'))
        else:
            print('Проверка не пройдена ошибка')
        return render(request, 'company/company_create.html', {"form": form})

class MainCompanyUpdate(BaseCompany):
    permission_required = ['admin']

    def get(self, request, pk):
        company = Company.objects.all().filter(user = request.user, id = pk).values()
        form = CompanyForm(company[0])
        return render(request, 'company/company_update.html', {"form": form})

    def post(self, request):
        # print(request.POST, request.FILES)
        form = CompanyForm(request.POST, request.FILES)
        # file = request.FILES['logo']
        if form.is_valid():
            cld =  form.cleaned_data
            upload_file_url = self.upload(cld['logo'], cld['id'])
            company = Company.objects.filter(id = cld['id'], user = request.user ).update(
                    type = cld['type_id'],
                    name = cld['name'],
                    ogrn = cld['ogrn'],
                    inn = cld['inn'],
                    telephon = cld['telephon'],
                    logo = upload_file_url,
                    url = cld['url'],
                    text = cld['text'],)
            return HttpResponseRedirect(reverse('main_company'))
        return render(request, 'company/company_update.html', {"form": form})

    def handle_uploaded_file(f):
        with open('some/file/name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

class MainCompanyDetail(BaseCompany):

    def get(self, request, pk):
        company = Company.objects.all().filter(user = request.user, id = pk).select_related()
        return render(request, 'company/company_detail.html', {"comp": company[0]})

class MainCompanyDelate(BaseCompany):

    def get(self, request, pk):
        pass


class MainWorkerList(PermissionGroupMixin, View):
    """docstring for Wokers."""
    permission_required = ['admin']

    def get(self, request):
        # user_id = request.user.id
        form = CompanyForm()
        # initial=[{ 'user_id': request.user.id }]
        return render(request, 'company/company_control.html', {"form": form})
