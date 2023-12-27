from rest_framework import serializers
from . models import Products, Customers, Branches, Employees

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'rating', 'decsription'] 
        
        
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'first_name', 'last_name', 'address', 'phone_number']
        
    
class BranchesSeializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['id', 'name', 'location']
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'full_name', 'job_title', 'sex']
        
        

        