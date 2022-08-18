from .models import Student
from django.core.mail import EmailMessage
from rest_framework import generics, status
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.views import View
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# def send_email(data):
#     email = EmailMessage(to=[data['to_email']],subject=data['email_subject'], body=data['email_body'])
#     email.send()
    