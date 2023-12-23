from django.contrib import admin
from .models import Products, Employees, Branches, Customers

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'rating', 'decsription')
    
admin.site.register(Products, ProductAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'sex')

admin.site.register(Employees, EmployeeAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

admin.site.register(Branches, BranchAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone_number')

admin.site.register(Customers, CustomerAdmin)



