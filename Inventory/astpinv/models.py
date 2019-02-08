from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    cnic = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname + '=>' + self.designation + '=>' + self.cnic


class StockEntry(models.Model):
    is_po_or_pettycash = models.CharField(max_length=100)
    po_number = models.CharField(max_length=100)
    scanner_id = models.CharField(max_length=100)
    po_company = models.CharField(max_length=100)
    date = models.DateField('Date')
    invoice_no = models.CharField(max_length=100)

    def __str__(self):
        return self.po_number


class Unit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    iname = models.CharField(max_length=100)
    iunit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    idept = models.ForeignKey(Department, on_delete=models.CASCADE)
    ise = models.ForeignKey(StockEntry, on_delete=models.CASCADE)
    iquantity = models.CharField(max_length=100)

    def __str__(self):
        return self.iname


class User(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.Emp.fullname


class IssuanceRecord(models.Model):
    req_name = models.ForeignKey(User, on_delete=models.CASCADE)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
