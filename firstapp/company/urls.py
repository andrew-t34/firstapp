from django.urls import path
from . import views



urlpatterns = [
    path('', views.MainCompanyList.as_view(), name="main_company"),
    path('activated/<int:pk>/', views.CompanyActivated.as_view(), name='company_activated'),
    path('create/', views.MainCompanyCreate.as_view(), name="company_create"),
    path('detail/<int:pk>/', views.MainCompanyDetail.as_view(), name="company_detail"),
    path('update/<int:pk>/', views.MainCompanyUpdate.as_view(), name="company_update"),
    path('update/', views.MainCompanyUpdate.as_view(), name="company_save_update"),
    #path("answers/<int:pk>/", views.GetAnswersForQuestion.as_view(), name="answers"),
]
