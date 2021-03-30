from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('student-form/', views.student_form, name="form" ),
    path('student-info/<student_id>', views.student_info, name="info" ),
    path('student-update/<student_id>', views.student_update, name="update" ),
    path('student-delete/<student_id>', views.student_delete, name="delete" ),
]