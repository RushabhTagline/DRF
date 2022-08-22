from django.urls import path
from Api import views

urlpatterns = [
    path('', views.StudentList.as_view()),  
    path('<int:id>/', views.StudentDetail.as_view()),
]