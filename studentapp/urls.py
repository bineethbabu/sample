from studentapp import views
from django.urls import path

urlpatterns=[
    path('',views.addstudent,name='addstudent'),
    path('addstudentdetails',views.addstudentdetails,name='addstudentdetails'),
    path('showstudent',views.showstudent,name='showstudent'),

   
    path('proflpage/<int:pk>',views.proflpage,name='proflpage'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('edit2sdtdetails/<int:pk>',views.edit2sdtdetails,name='edit2sdtdetails'),
    path('deletestudent/<int:pk>',views.deletestudent,name='deletestudent'),
    path('delete/<int:pk>',views.delete,name='delete'),
]
