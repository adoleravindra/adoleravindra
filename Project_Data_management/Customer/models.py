from django.db import models

# Customer Details
class Customer(models.Model):
    CompanyName = models.CharField(max_length=20)
    EmployeeID= models.IntegerField(primary_key=True)
    CustomerName = models.CharField(max_length=30)
    ContactNumber = models.IntegerField()
    Email = models.EmailField()
    PW = models.CharField(max_length=20)

# Product order Details
class Product(models.Model):
    CompanyName = models.CharField(max_length=20)
    ProName = models.CharField(max_length=50)
    orderdate = models.DateField()
    EmployeeID = models.IntegerField(primary_key=True)
    CustName = models.CharField(max_length=30)
    OrderQty = models.IntegerField()
    Material = models.CharField(max_length=100)
    Equipement = models.CharField(max_length=100)



