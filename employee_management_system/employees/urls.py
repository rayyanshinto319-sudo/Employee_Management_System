from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('logout-success/', views.logout_success, name='logout_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employee/add/', views.add_employee, name='add_employee'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/<int:pk>/edit/', views.edit_employee, name='edit_employee'),
    path('employee/<int:pk>/delete/', views.delete_employee, name='delete_employee'),
    path('change-password/', views.change_password, name='change_password'),
]
