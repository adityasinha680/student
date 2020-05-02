from django.shortcuts import render
from schoolapp import models
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
	
	student_details=models.Details.objects.all()
	data={
		'student_details':student_details

	}
	return render(request,'schoolapp/index.html',context=data)


def addstudent(request):
	if request.method =='POST':
		first_name= request.POST['fname']
		last_name= request.POST['lname']
		email = request.POST['email']
		data =models.Details(fname=first_name,lname=last_name,email=email)
		data.save()
		return HttpResponseRedirect(reverse('schoolapp:index'))
	return render(request,'schoolapp/addstudent.html')


def edit_student(request,pk):
	return render(request,'schoolapp/edit_student')



