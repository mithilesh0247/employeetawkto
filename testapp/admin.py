from django.contrib import admin
from testapp.models import Employee,ProxyEmployee
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['id','eno','ename','esal','eaddr']
# Register your models here.
class ProxyEmployeeAdmin(admin.ModelAdmin):
	list_display=['id','eno','ename','esal','eaddr']



admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)
