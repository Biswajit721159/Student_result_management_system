
from django.contrib import admin
from django.urls import path,include
from srms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('show_result',views.show_result),
    path('<str:roll_no>/Feedback/',views.Feedback__),
    path('<str:roll_no>/Submit_Feedback/',views.Feedback_from),
    path('adminpanel/',include('student.urls'))
]
