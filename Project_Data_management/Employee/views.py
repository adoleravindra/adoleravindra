from django.shortcuts import render
from django.core.mail import send_mail
import Project_Data_management.settings
from Employee.models import Employee
from Employee.models import Store
from Employee.models import Soldering
from Employee.models import Production_Testing
from Employee.models import Quality

# Employee Signup Details
def EmpSignup(request):
    try:
        EmpID = request.POST.get("EmpID")
        EmpName = request.POST.get("EmpName")
        Cno = request.POST.get("Cno")
        Email = request.POST.get("email")
        Password = request.POST.get("PW")
        cpassword = request.POST.get("CPW")
        if Password == cpassword:
            Employee(EmployeeID=EmpID,EmployeeName=EmpName,ContactNo=Cno,Email=Email,PW=Password).save()
            return render(request,"Employee/Employee.html")
        else:
            return render(request, "Employee/EmpSignup.html", {"msg": "Password Does Not Match Re-entered Details"})
    except ValueError:
        return render(request,"Employee/EmpSignup.html")

# Check login Details
def checkEmp(request):
    try:
        EmpID = request.POST.get("ID")
        password = request.POST.get("CPW")
        try:
            res = Employee.objects.get(EmployeeID=EmpID)
            if EmpID == str(res.EmployeeID) and password == res.PW:
                return render(request,"Employee/store.html")
            else:
                return render(request,"Employee/Employee.html",{"msg":"Invalid Employee ID and Password"})
        except Employee.DoesNotExist:
            return render(request, "Employee/Employee.html")
    except ValueError:
        return render(request, "Employee/Employee.html")

# Save Store Department Details in database
def storeDep(request):
    try:
        ProName = request.POST.get("ProName")
        EmpID = request.POST.get("EmpID")
        EmpName = request.POST.get("EmpName")
        Department = request.POST.get("Department")
        List = request.POST.get("List")
        date = request.POST.get("date")
        Store(ProductName=ProName,EmployeeID=EmpID,EmployeeName=EmpName,Department=Department,MaterialListQty=List,date=date).save()
        return render(request,"index.html")
    except ValueError:
        return render(request,"Employee/store.html")

# Save Soldering Department Details in database
def solderingDep(request):
    try:
        ProName = request.POST.get("ProName")
        EmpID = request.POST.get("EmpID")
        EmpName = request.POST.get("EmpName")
        TargetQty = request.POST.get("TargetQty")
        RecMatList = request.POST.get("RecMatList")
        date = request.POST.get("date")
        ComBoardQty = request.POST.get("ComBoardQty")
        RewBorQty = request.POST.get("RewBorQty")
        Soldering(ProductName=ProName,EmployeeID=EmpID,EmployeeName=EmpName,TargetQty=TargetQty,RecMatQty=RecMatList,
                  ComBorQty=ComBoardQty,RewBorQty=RewBorQty,date=date).save()
        return render(request,"index.html")
    except ValueError:
        return render(request,"Employee/soldering.html")

# Save Final Production and Testing Department Details in database
def ProTestDep(request):
    try:
        ProName = request.POST.get("ProName")
        EmpID = request.POST.get("EmpID")
        EmpName = request.POST.get("EmpName")
        TargetQty = request.POST.get("TargetQty")
        date = request.POST.get("date")
        RecBoardQty = request.POST.get("RecBoardQty")
        TestBoardQty = request.POST.get("TestBoardQty")
        ReworkBoardQty = request.POST.get("ReworkBoardQty")
        CompBoardQty = request.POST.get("ComBoardQty")
        Production_Testing(ProductName=ProName,EmployeeID=EmpID,EmployeeName=EmpName,TargetQty=TargetQty,date=date,
                           RecBorQty=RecBoardQty,RewBorQty=ReworkBoardQty,ComBorQty=CompBoardQty,TestBorQty=TestBoardQty).save()
        return render(request,"index.html")
    except ValueError:
        return render(request,"Employee/testing.html")

# Save Quality Department Details in database
def qualityDep(request):
    try:
        ProName = request.POST.get("ProName")
        EmpID = request.POST.get("EmpID")
        EmpName = request.POST.get("EmpName")
        TargetQty = request.POST.get("TargetQty")
        date = request.POST.get("date")
        RecBoardQty = request.POST.get("RecBoardQty")
        testBoardQty= request.POST.get("testBoardQty")
        ReworkBoardQty = request.POST.get("ReworkBoardQty")
        CompletedBoardQty = request.POST.get("CompletedBoardQty")
        print(EmpID)
        Quality(ProductName=ProName,EmployeeID=EmpID,EmployeeName=EmpName,TargetQty=TargetQty,date=date,
                RecBorQty=RecBoardQty,TestBorQty=testBoardQty,RewBorQty=ReworkBoardQty,ComBorQty=CompletedBoardQty).save()
        return render(request,"index.html")
    except ValueError:
        return render(request,"Employee/quality.html")

# forgot password
def checkEmpPassword(request):
    try:
        id = request.POST.get("ID")
        if request.method =='POST':
            Email = Employee.objects.get(Email=id)
            if Email.Email == id:
                mail_to = [Email.Email]
                send_mail("Login Password",
                          "Employee Name:"+Email.EmployeeName+"\n"+"Employee ID:"+str(Email.EmployeeID)+"\n"+"Password:"+Email.PW,
                          Project_Data_management.settings.EMAIL_HOST_USER,
                          mail_to)
            return render(request,"Employee/forgotPassword.html",{"msg":"Password is send to your Email ID"})

    except Employee.DoesNotExist:
        return render(request,"Employee/Employee.html")