from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo, name='home'),
    path('test',views.testing, ),
    
    path('form1',views.form1, name='form1'),
    path('form2/<int:id>',views.form2, name='form2')
]