from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from rest_framework import generics 

from .Serializers import Todo_serializer
# Create your views here.
def home(request):
    return render(request, "home.html")
class todoData(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todo_serializer

class UpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = Todo.objects.all()
        serializer_class = Todo_serializer
    


