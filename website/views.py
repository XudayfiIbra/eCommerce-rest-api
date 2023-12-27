from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . serializers import ProductSerializer, CustomerSerializer, BranchesSeializer, EmployeeSerializer
from . models import Products, Customers, Branches, Employees


@api_view(['GET', 'POST'])
def api_products(request):  
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
    

@api_view(['GET', 'PUT', 'DELETE'])
def api_products_info(request, id):
    
    try:
        products = Products.objects.get(pk=id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(products)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
@api_view (['GET', 'POST'])
def api_customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        # what does mean many=true? is used when we dealing with more than one object
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view (['GET', 'PUT', 'DELETE'])
def api_customers_info(request, id):
    try:
        customer = Customers.objects.get(pk=id)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view (['GET', 'POST'])
def api_branches(request):
    if request.method == 'GET':
        branch = Branches.objects.all()
        serializer = BranchesSeializer(branch, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BranchesSeializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view (['GET', 'PUT', 'DELETE'])
def api_branches_info(request, id):
    try:
        branch = Branches.objects.get(pk=id)
    except Branches.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BranchesSeializer(branch)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BranchesSeializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view (['GET', 'POST'])   
def api_employees(request):
    if request.method == 'GET':
        employee = Employees.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view (['GET', 'PUT', 'DELETE'])
def api_employees_info(request, id):
    try:
        employees = Employees.objects.get(pk=id)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)