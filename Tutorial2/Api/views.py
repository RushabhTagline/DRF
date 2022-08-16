from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer
# Create your views here.


class Studentlist(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer