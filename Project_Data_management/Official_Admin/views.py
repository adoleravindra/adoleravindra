import csv
from django.shortcuts import render,HttpResponse
from Employee.models import Soldering, Production_Testing, Quality,Store
from Customer.models import Product,Customer
from django.core.mail import send_mail
import Project_Data_management.settings

# TeamLeader Login
def checkTL(request):
    try:
        id = request.POST.get("ID")
        pw = request.POST.get("PW")
        department = request.POST.get("Department")
        if id == "teamleader" and pw == "teamleader" and department == "Soldering":
            sold = Soldering.objects.all()
            return render(request,"Official_Admin/solderingTL.html",{"data":sold})
        elif id == "teamleader" and pw == "teamleader" and department =="Final Production and Testing":
            production = Production_Testing.objects.all()
            return render(request, "Official_Admin/productionTL.html",{"data":production})
        elif id == "teamleader" and pw == "teamleader" and department == "Quality":
            quality = Quality.objects.all()
            return render(request, "Official_Admin/qualityTL.html",{"data":quality})
        else:
            return render(request, "Official_Admin/TL.html")
    except ValueError:
        return render(request,"Official_Admin/TL.html")

# Supervisor Login
def checkSupervisor(request):
    try:
        id = request.POST.get("ID")
        pw = request.POST.get("PW")
        dep = request.POST.get("Department")
        if id == "supervisor" and pw == "supervisor" and dep == "Soldering":
            sold = Soldering.objects.all()
            return render(request,"Official_Admin/supervisor_soldering.html",{"data":sold})
        elif id == "supervisor" and pw == "supervisor" and dep == "Final Production and Testing":
            production = Production_Testing.objects.all()
            return render(request, "Official_Admin/supervisor_production.html",{"data":production})
        elif id == "supervisor" and pw == "supervisor" and dep == "Quality":
            quality = Quality.objects.all()
            return render(request, "Official_Admin/supervisor_quality.html",{"data":quality})
        else:
            return render(request,"Official_Admin/supervisor.html")
    except ValueError:
        return render(request,"Official_Admin/supervisor.html")


# Manager Login
def checkManager(request):
    try:
        id = request.POST.get("ID")
        pw = request.POST.get("PW")
        if id == "manager" and pw == "manager":
            store = Store.objects.all()
            proOrder = Product.objects.all()
            soldering = Soldering.objects.all()
            production = Production_Testing.objects.all()
            quality = Quality.objects.all()
            return render(request, "Official_Admin/__manager__.html",{"data4":store,"data":proOrder,"data1":soldering,"data2":production,"data3":quality})
        else:
            return render(request, "Official_Admin/Admin.html")
    except ValueError:
        return render(request, "Official_Admin/Admin.html")

# Sending Mail
def sendMail(request):
    try:
        id = request.POST.get("id")
        proOrder = Product.objects.get(EmployeeID=id)
        mail_to = ["ravindraadole1804@gmail.com","rahulgawali1511@gmail.com"]
        send_mail("About Place Order from Customer","Customer Product Details\n"+
            "Company Name: "+ str(proOrder.CompanyName)+"\n"+"Product Name: "+str(proOrder.ProName)+"\n"+"Product Order Quantity: "+str(proOrder.OrderQty)+"\n \n from Manager",
        Project_Data_management.settings.EMAIL_HOST_USER,mail_to)
        return render(request,"Official_Admin/__manager__.html",{"data":proOrder})
    except TypeError:
        return render(request, "Official_Admin/Admin.html")


def downloadSoldering(request):
    res = Soldering.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="solderingDepartmentDetails.csv"'
    writer = csv.writer(response, delimiter =",")
    writer.writerow(['Product Name','Employee ID','Employee Name','Target Quantity','Received Material Quantity','date','Completed Board Quantity','Rework Board Quantity'])
    for obj in res:
        writer.writerow([obj.ProductName,obj.EmployeeID,obj.EmployeeName,obj.TargetQty,obj.RecMatQty,obj.date,obj.ComBorQty,obj.RewBorQty])
    return response


def downloadProduction(request):
    res = Production_Testing.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ProductionDepartmentDetails.csv"'
    writer = csv.writer(response, delimiter=",")
    writer.writerow(
        ['Product Name', 'Employee ID', 'Employee Name', 'Target Quantity','date', 'Received Board Quantity', 'Tested Board Quantity', 'Rework Board Quantity',
         'Completed Board Quantity'])
    for obj in res:
        writer.writerow(
            [obj.ProductName, obj.EmployeeID, obj.EmployeeName, obj.TargetQty, obj.date,  obj.RecBorQty,obj.TestBorQty,
             obj.RewBorQty,obj.ComBorQty])
    return response


def downloadQuality(request):
    res = Quality.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="qualityDepartmentDetails.csv"'
    writer = csv.writer(response, delimiter=",")
    writer.writerow(
        ['Product Name', 'Employee ID', 'Employee Name', 'Target Quantity', 'date', 'Received Board Quantity',
         'Tested Board Quantity', 'Rework Board Quantity',
         'Completed Board Quantity'])
    for obj in res:
        writer.writerow(
            [obj.ProductName, obj.EmployeeID, obj.EmployeeName, obj.TargetQty, obj.date, obj.RecBorQty, obj.TestBorQty,
             obj.RewBorQty, obj.ComBorQty])
    return response