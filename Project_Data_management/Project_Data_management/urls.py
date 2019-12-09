"""Project_Data_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView
from Official_Admin import views as Admin_view
from Employee import views as Emp_view
from Customer import views as Customer_view

urlpatterns = [
    path('index/',TemplateView.as_view(template_name="index.html")),
    path('Admin/',TemplateView.as_view(template_name="Official_Admin/Admin.html")),
    path('Employee/',TemplateView.as_view(template_name="Employee/Employee.html")),
    path('Customer/',TemplateView.as_view(template_name="Customer/Customer.html")),
    path('EmpSignup/',TemplateView.as_view(template_name="Employee/EmpSignup.html")),
    path('forgotPassword/',TemplateView.as_view(template_name="Employee/forgotPassword.html")),
    path('forgotPassword2/',TemplateView.as_view(template_name="Customer/forgotpassword.html")),
    path('EmpDetails/',Emp_view.EmpSignup),
    path('CustomerSignup/',TemplateView.as_view(template_name="Customer/CustomerSignup.html")),
    path('checkEmp/', Emp_view.checkEmp),
    path('CustomerDetails/', Customer_view.CustomerSignup),
    path('checkCustomer/', Customer_view.checkCustomer),
    path('Admin_Logout/',TemplateView.as_view(template_name="index.html")),
    path('Employee_Logout/', TemplateView.as_view(template_name="index.html")),
    path('quality/',TemplateView.as_view(template_name="Employee/quality.html")),
    path('soldering/',TemplateView.as_view(template_name="Employee/soldering.html")),
    path('testing/', TemplateView.as_view(template_name="Employee/testing.html")),
    path('store/', TemplateView.as_view(template_name="Employee/store.html")),
    path('customerProduct/',TemplateView.as_view(template_name="Customer/CustomerProduct.html")),
    path('manager/',TemplateView.as_view(template_name="Official_Admin/Admin.html")),
    path('supervisor/',TemplateView.as_view(template_name="Official_Admin/supervisor.html")),
    path('TL/', TemplateView.as_view(template_name="Official_Admin/TL.html")),
    path('orderProduct/',Customer_view.orderProduct),
    path('ProductLogout/',TemplateView.as_view(template_name="index.html")),
    path('storeDep/',Emp_view.storeDep),
    path('solderingDep/',Emp_view.solderingDep),
    path('ProTestDep/',Emp_view.ProTestDep),
    path('qualityDep/',Emp_view.qualityDep),
    path('checkTL/',Admin_view.checkTL),
    path('checkSupervisor/',Admin_view.checkSupervisor),
    path('checkManager/',Admin_view.checkManager),
    path('sendMail/',Admin_view.sendMail),
    path('checkEmpPassword/',Emp_view.checkEmpPassword),
    path('checkCustomerPassword/',Customer_view.checkCustomerPassword),
    path('downloadSoldering/',Admin_view.downloadSoldering),
    path('downloadProduction/',Admin_view.downloadProduction),
    path('downloadQuality/',Admin_view.downloadQuality)
]
