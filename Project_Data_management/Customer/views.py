from django.core.mail import send_mail
from django.shortcuts import render
import Project_Data_management.settings
from Customer.models import Customer, Product

# Customer Signup Details
def CustomerSignup(request):
    try:
        name_com = request.POST.get("CompanyName")
        id = request.POST.get("EmpID")
        name_cust = request.POST.get("CustomerName")
        contact = request.POST.get("Cno")
        email = request.POST.get("email")
        password = request.POST.get("PW")
        cpassword = request.POST.get("CPW")
        if password == cpassword:
            Customer(CompanyName=name_com, EmployeeID=id, CustomerName=name_cust, ContactNumber=contact, Email=email,
                     PW=password).save()
            return render(request, "Customer/Customer.html")
        else:
            return render(request, "Customer/CustomerSignup.html",
                          {"msg": "Password Does Not Match Re-entered Details"})
    except ValueError:
        return render(request, "Customer/CustomerSignup.html")

# check details for login
def checkCustomer(request):
    try:
        EmpID = request.POST.get("EmpID")
        Password = request.POST.get("PW")
        try:
            res = Customer.objects.get(EmployeeID=EmpID)
            if EmpID == str(res.EmployeeID) and Password == res.PW:
                return render(request, "Customer/CustomerProduct.html")
            else:
                return render(request, "Customer/Customer.html", {"msg": "Invalid Customer ID and Password"})
        except Customer.DoesNotExist:
            return render(request, "Customer/Customer.html")
    except ValueError:
        return render(request,"Customer/Customer.html")

# Product order details
def orderProduct(request):
    try:
        if request.method == 'POST':
            comName = request.POST.get("CompanyName")
            ProName = request.POST.get("ProductName")
            date = request.POST.get("date")
            id = request.POST.get("id")
            CustomerName = request.POST.get("CustomerName")
            qty = request.POST.get("qty")
            material = request.POST.get("material")
            equipment = request.POST.get("equipment")
            Product(CompanyName=comName,ProName=ProName,orderdate=date,EmployeeID=id,CustName=CustomerName,
                    OrderQty=qty,Material=material,Equipement=equipment).save()
            return render(request,"Customer/CustomerProduct.html")
    except ValueError:
        return render(request,"Customer/CustomerProduct.html")

# forgot password
def checkCustomerPassword(request):
    try:
        id = request.POST.get("ID")
        if request.method =='POST':
            Email = Customer.objects.get(Email=id)
            if Email.Email == id:
                mail_to = [Email.Email]
                send_mail("Login Password",
                          "Customer Name:"+Email.CustomerName+"\n"+"Employee ID:"+str(Email.EmployeeID)+"\n"+"Password:"+Email.PW,
                          Project_Data_management.settings.EMAIL_HOST_USER,
                          mail_to)
            return render(request,"Customer/forgotpassword.html",{"msg":"Password is send to your Email ID"})

    except Customer.DoesNotExist:
        return render(request,"Customer/Customer.html")


