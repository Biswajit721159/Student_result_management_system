
from django.contrib import admin
from django.urls import path,include
from student import views

urlpatterns = [
    
    path('',views.index), 
    path('connect',views.connect),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.Logout),
    path('logoutpage',views.logoutpage),

    #manageclass

    path('manageclass',views.manageclass),
    path('manageclass/addclass',views.addclass),
    path('manageclass/submit_data',views.submit_data),
    path('manageclass/search_class_id',views.manage_search_class_id),
    path('manageclass/search_class_name',views.manage_search_class_name),
    path('manageclass/search_section',views.manage_search_section),
    path('manageclass/search_class_name_numeric',views.manage_search_class_name_numeric),
    path('manageclass/update/<int:class_id>',views.class_update),
    path('manageclass/delete/<int:class_id>',views.class_delete),
    path('manageclass/update/<int:class_id>/submit_updated_data',views.manage_class_submit_updated_data),


]
