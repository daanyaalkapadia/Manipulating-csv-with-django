from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addstudent/', views.add_student,name='addstudent'),
    path('displayallstudent/', views.display_all_student,name='displayallstudent'),
    path('searchstudent/', views.search_student,name='searchstudent'),
]