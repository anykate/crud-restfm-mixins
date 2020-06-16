from django.urls import path
from . import views


app_name = 'crudmixins'

urlpatterns = [
    path('', views.savestudent, name='save_student_data'),
    path('api/students/', views.StudentListCreate.as_view(),
         name='list_create_student_data_api'),
    path('api/students/<int:student_id>/', views.StudentRetrieveUpdateDestroy.as_view(),
         name='retrieve_update_destroy_student_data_api'),
]
