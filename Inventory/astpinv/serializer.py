from rest_framework import serializers
from .models import Department, Employee, StockEntry, Unit, Item, User, IssuanceRecord


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
        def create(self, validated_data):
            return Department.objects.create(**validated_data)


class EmployeeSerializer(serializers.ModelSerializer):
    deptn = serializers.SerializerMethodField('deptname')
    
    def deptname(self, employee):
        return employee.dept.name
    
    class Meta:
        model = Employee
        fields = ['dept', 'fullname', 'designation', 'cnic', 'mobile', 'deptn']
    
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


class StockEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockEntry
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    conunit = serializers.SerializerMethodField('unitname')
    condept = serializers.SerializerMethodField('deptname')
    conse = serializers.SerializerMethodField('sename')
    
    def unitname(self, item):
        return item.iunit.name
    
    def deptname(self, item):
        return item.idept.name
    
    def sename(self, item):
        return item.ise.po_number
    
    class Meta:
        model = Item
        fields = ['id', 'iname', 'iunit', 'idept', 'ise', 'iquantity', 'conunit', 'condept', 'conse']


class UserSerializer(serializers.ModelSerializer):
    condept = serializers.SerializerMethodField('dept_name')
    conEmp = serializers.SerializerMethodField('empname')
    
    def dept_name(self, user):
        return user.dept.name
    
    def empname(self, user):
        return user.Emp.fullname
    
    class Meta:
        model = User
        fields = ['Emp', 'dept', 'username', 'password', 'condept', 'conEmp']


class IssuanceRecordSerializer(serializers.ModelSerializer):
    conreq_name = serializers.SerializerMethodField('req_name1')
    conemp = serializers.SerializerMethodField('empname')
    conitem = serializers.SerializerMethodField('itemname')
    
    def req_name1(self, ir):
        return ir.req_name.Emp.fullname
    
    def empname(self, ir):
        return ir.emp.fullname
    
    def itemname(self, ir):
        return ir.item.iname
    
    class Meta:
        model = IssuanceRecord
        fields = ['req_name', 'emp', 'item', 'quantity', 'conreq_name', 'conemp', 'conitem']
