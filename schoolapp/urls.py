from django.urls import path
from . import views
app_name = 'schoolapp'

urlpatterns=[
	path('',views.index, name='index'),
	path('addstudent/',views.addstudent,name='addstudent'),
	path('edit_student/<pk>/',views.edit_student,name="edit_student")

]