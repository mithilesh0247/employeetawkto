from django.db import models

# Create your models here.
class CustomManager1(models.Manager):
	def get_queryset(self):
		return super().get_queryset().order_by('-esal')
	#def get_emp_sal_range(self,esal1,esal2):
	#	return super().get_queryset().filter(esal__range=(esal1,esal2)).order_by('esal')
	#def get_emp_sorted_by(self,param):
	#	return super().get_queryset().order_by(param)
class CustomManager2(models.Manager):
	def get_queryset(self):
	    return super().get_queryset().order_by('ename')

			
class Employee(models.Model):
	eno=models.IntegerField()
	ename=models.CharField(max_length=(40))
	esal=models.FloatField()
	eaddr=models.CharField(max_length=(50))
	objects=CustomManager1()
	'''Proxy models inhance the utilization of models 
	it means we cutomized our table as per our needs 
	it means we provide multiple view of existing table '''
class ProxyEmployee(Employee):
	objects=CustomManager2()
	class Meta:
		proxy=True








