from django.urls import path
from user_data import views


urlpatterns = [
    path('students/', views.student_data_list),
    path('students/<int:pk>/', views.student_specific),
]
