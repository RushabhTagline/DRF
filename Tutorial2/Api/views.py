from .models import Student
from django.core.mail import EmailMessage
from rest_framework import generics, status
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class StudentList(generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        items = Student.objects.all()
        serializer = StudentSerializer(items, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            email_body = 'Error : ' + str(serializer.errors)
            data = {
                'to_email': "rushabh.tagline@yopmail.com",
                'email_body': email_body,
                'email_subject': 'Verify your Code'
                }
            send_email(data)
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, id, *args, **kwargs):
        if id:
            item = Student.objects.get(id=id)
            serializer = StudentSerializer(item)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, *args, **kwargs):
        item = Student.objects.get(id=id)
        serializer = StudentSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            email_body = 'Error : ' + str(serializer.errors)
            data = {
                'to_email': "rushabh.tagline@yopmail.com",
                'email_body': email_body,
                'email_subject': 'Verify your Code'
                }
            send_email(data)
            return Response({"status": "error", "data": serializer.errors})
    
    def delete(self, request, id):
        item = get_object_or_404(Student, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

def send_email(data):
    email = EmailMessage(to=[data['to_email']],subject=data['email_subject'], body=data['email_body'])
    email.send()
    