from django.db import models

# Employee Details
class Employee(models.Model):
    EmployeeName = models.CharField(max_length=30)
    EmployeeID = models.IntegerField(primary_key=True)
    ContactNo = models.IntegerField()
    Email = models.EmailField()
    PW = models.CharField(max_length=15)

# Store Department Details
class Store(models.Model):
    ProductName = models.CharField(max_length=30)
    EmployeeID = models.IntegerField(primary_key=True)
    EmployeeName = models.CharField(max_length=30)
    Department = models.CharField(max_length=30)
    MaterialListQty = models.CharField(max_length=1000)
    date = models.DateField()

# Soldering Department Details
class Soldering(models.Model):
    ProductName = models.CharField(max_length=30)
    EmployeeID = models.IntegerField(primary_key=True)
    EmployeeName = models.CharField(max_length=30)
    TargetQty = models.IntegerField()
    RecMatQty = models.CharField(max_length=1000)
    date = models.DateField()
    ComBorQty = models.IntegerField()
    RewBorQty = models.IntegerField()

# Final Production and Testing Department Details
class Production_Testing(models.Model):
    ProductName = models.CharField(max_length=30)
    EmployeeID = models.IntegerField(primary_key=True)
    EmployeeName = models.CharField(max_length=30)
    TargetQty = models.IntegerField()
    date = models.DateField()
    RecBorQty = models.IntegerField()
    TestBorQty = models.IntegerField()
    RewBorQty = models.IntegerField()
    ComBorQty = models.IntegerField()

# Quality Department
class Quality(models.Model):
    ProductName = models.CharField(max_length=30)
    EmployeeID = models.IntegerField(primary_key=True)
    EmployeeName = models.CharField(max_length=30)
    TargetQty = models.IntegerField()
    date = models.DateField()
    RecBorQty = models.IntegerField()
    TestBorQty = models.IntegerField()
    RewBorQty = models.IntegerField()
    ComBorQty = models.IntegerField()
