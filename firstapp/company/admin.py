from django.contrib import admin

from company.models import Type, Company, Division, Worker
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ("name_short", "name_long")
    list_filter = ("name_long",)

admin.site.register(Type, TypeAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("user_id", "name", "ogrn", "inn", "date_create")
    list_filter = ("date_create",)

admin.site.register(Company, CompanyAdmin)


class DivisionAdmin(admin.ModelAdmin):
    list_display = ("company_id", "name")
    list_filter = ("company_id",)

admin.site.register(Division, DivisionAdmin)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ("full_name_worker", "job_position", "snils")
    list_filter = ("company",)

admin.site.register(Worker, WorkerAdmin)
