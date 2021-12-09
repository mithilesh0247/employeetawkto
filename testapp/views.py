from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count
from django.db.models.functions import Lower
# Create your views here.
def index(request):
	return render(request,'index.html')
def empview(request):
	#emp_list=Employee.objects.all()
	#emp_list=Employee.objects.filter(esal__=[::-2])
	#emp_list=Employee.objects.filter(esal__lt=2000)
	#emp_list=Employee.objects.all().order_by('ename')
	#emp_list=Employee.objects.all().order_by(Lower('ename'))
	emp_list=Employee.objects.get_queryset().order_by('-esal')
	#emp_list=Employee.objects.filter('esal')[0::1]
	my_dict={'emp_list':emp_list}
	return render(request,'employee.html',context=my_dict)




