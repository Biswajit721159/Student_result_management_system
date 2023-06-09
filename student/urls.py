
from django.contrib import admin
from django.urls import path,include
from student import views

urlpatterns = [
    
    path('',views.index), 
    path('connect',views.connect),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.Logout),
    path('logoutpage',views.logoutpage),
    path('search_top_candidates',views.search_top_candidates),
    path('search_class_name_to_find_top_candidates',views.search_class_name_to_find_top_candidates),

    #manage_reviews
    path('manage_reviews',views.manage_reviews),
    path('manage_reviews/delete/<str:Reviews_id>',views.delete_Reviews),

    #manage_feedback
    path('manage_feedback',views.manage_feedback),
    path('manage_feedback/delete/<str:Feedback_id>',views.delete_feedback),
    #manageclass

    path('manageclass',views.manageclass),
    path('manageclass/addclass',views.addclass),
    path('manageclass/submit_data',views.submit_data),
    path('manageclass/search_class_id',views.manageclass_search_class_id),
    path('manageclass/search_class_name',views.manageclass_search_class_name),
    path('manageclass/search_class_name_numeric',views.manageclass_search_class_name_numeric),
    path('manageclass/update/<int:class_id>',views.class_update),
    path('manageclass/delete/<int:class_id>',views.class_delete),
    path('manageclass/update/<int:class_id>/submit_updated_data',views.manage_class_submit_updated_data),

    #managestudent
    path('managestudent',views.managestudent),
    path('managestudent/addstudent',views.addstudent),
    path('managestudent/student_submit_data',views.student_submit_data),
    path('managestudent/delete/<int:student_id>',views.delete_student),
    path('managestudent/update/<int:student_id>',views.update_student),
    path('managestudent/update_student_submit_data/<int:student_id>',views.update_student_submit_data),
    path('managestudent/search_student_id',views.manage_search_student_id),
    path('managestudent/search_class_name',views.manage_search_class_name),
    path('managestudent/search_roll_no',views.manage_search_roll_no),
    path('managestudent/search_name',views.manage_search_name),
    path('managestudent/search_email',views.manage_search_email),
    path('managestudent/search_gendar',views.manage_search_gendar),
    path('managestudent/search_dob',views.manage_search_dob),
    
    #managesubject
    path('managesubject',views.managesubject),
    path('managesubject/search_subject_id',views.subject_search_subject_id),
    path('managesubject/search_subject_name',views.subject_search_subject_name),
    path('managesubject/search_subject_code',views.subject_search_subject_code),
    path('managesubject/delete/<int:subject_id>',views.delete_subject),
    path('managesubject/addsubject',views.add_subject),
    path('managesubject/submit_data',views.subject_submit_data),
    path('managesubject/update/<int:subject_id>',views.subject_update_data),
    path('managesubject/update/submit_subject_updated_data/<int:subject_id>',views.submit_subject_updated_data),

    #subject_com

    path('manage_subject_com',views.manage_subject_com),
    path('manage_subject_com/delete/<int:subject_com_id>',views.delete_subject_com),
    path('manage_subject_com/add_subject_com',views.manage_add_subject_com),
    path('manage_subject_com/subject_com_submit_data',views.subject_com_submit_data),
    path('manage_subject_com/search_subject_com_id',views.manage_com_search_subject_com_id),
    path('manage_subject_com/search_class_name',views.manage_com_search_class_name),
    path('manage_subject_com/search_subject_name',views.manage_com_search_subject_name),


    #manage_result
    path('manage_result',views.manage_result),
    path('manage_result/<str:class_name>/manage_result_add_data',views.manage_result_add_data),
    path('manage_result/addresult',views.addresult),
    path('manage_result/delete/<int:result_id>',views.delete_result),
    path('manage_result/search_class_name_to_add',views.search_class_name_to_add),
    path('manage_result/search_result_id',views.manage_result_search_result_id),
    path('manage_result/search_student_name',views.manage_result_search_student_name),
    path('manage_result/search_class_name',views.manage_result_search_class_name),
    path('manage_result/search_roll_no',views.manage_result_search_roll_no),
    path('manage_result/search_subject_name',views.manage_result_search_subject_name),
    path('manage_result/search_marks',views.manage_result_search_marks),
    path('manage_result/update/<str:result_id>',views.update_result),
    path('manage_result/manage_update_submit/<str:result_id>',views.manage_update_submit),

]
