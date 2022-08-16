from django.urls import path
from Api import views

urlpatterns = [
    path('',views.Studentlist.as_view()),
    path('<int:pk>/',views.Studentdetails.as_view()),
]