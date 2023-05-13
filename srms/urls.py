
from django.contrib import admin
from django.urls import path,include
from srms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('adminpanel/',include('student.urls'))
]
