from .models import Department, Employee, StockEntry, Unit, Item, User, IssuanceRecord
from .serializer import DepartmentSerializer, EmployeeSerializer, UserSerializer, IssuanceRecordSerializer, \
    UnitSerializer, StockEntrySerializer, ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class DisplayDept(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        dept = Department.objects.all()
        serializer = DepartmentSerializer(dept, many=True)
        return Response(serializer.data)

    def post(self, request):
        recdept = request.data
        department_serializer = DepartmentSerializer(data=recdept)
        if department_serializer.is_valid(raise_exception=True):
            department_serializer.save()
            return Response(department_serializer.data)


class DisplayEmp(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request):
        recemp = request.data
        employee_serializer = EmployeeSerializer(data=recemp)
        if employee_serializer.is_valid(raise_exception=True):
            employee_serializer.save()
            return Response(employee_serializer.data)


class DisplayStockEntry(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        se = StockEntry.objects.all()
        serializer = StockEntrySerializer(se, many=True)
        return Response(serializer.data)

    def post(self, request):
        recse = request.data
        stockentry_serializer = StockEntrySerializer(data=recse)
        if stockentry_serializer.is_valid(raise_exception=True):
            stockentry_serializer.save()
            return Response(stockentry_serializer.data)


class DisplayItem(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request):
        recitem = request.data
        item_serializer = ItemSerializer(data=recitem)
        if item_serializer.is_valid(raise_exception=True):
            item_serializer.save()
            return Response(item_serializer.data)


class DisplayIssuanceRecord(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        ir = IssuanceRecord.objects.all()
        serializer = IssuanceRecordSerializer(ir, many=True)
        return Response(serializer.data)

    def post(self, request):
        recir = request.data
        issuancerecord_serializer = IssuanceRecordSerializer(data=recir)
        if issuancerecord_serializer.is_valid(raise_exception=True):
            issuancerecord_serializer.save()
            return Response(issuancerecord_serializer.data)


class DisplayUnit(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        unit = Unit.objects.all()
        serializer = UnitSerializer(unit, many=True)
        return Response(serializer.data)

    def post(self, request):
        recunit = request.data
        unit_serializer = UnitSerializer(data=recunit)
        if unit_serializer.is_valid(raise_exception=True):
            unit_serializer.save()
            return Response(unit_serializer.data)


class DisplayUser(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        recuser = request.data
        user_serializer = UserSerializer(data=recuser)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response(user_serializer.data)
