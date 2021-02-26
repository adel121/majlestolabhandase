from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views 

urlpatterns = [
    path('',views.index, name="index"),
    path('Courses/<int:PK>/',views.course_list, name="course_list"),
    path('Course_Prompt/<str:name>/',views.course_prompt, name="course_prompt"),
    path('Course_Videos/<str:name>/',views.course_videos,name="course_videos"),
    path('Course_Documents/<str:name>/',views.course_documents,name="course_documents"),
    path('Class_List/<str:discipline>/', views.class_list, name="class_list")
]
