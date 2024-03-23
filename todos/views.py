from django.shortcuts import render, HttpResponse, redirect

# todos/views.py
from rest_framework import generics

from .models import Todo, Schedule
from .forms import TodoForm
from .serializers import TodoSerializer, ScheduleSerializer
from rest_framework.response import Response

class ListTodoView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# list all tasks
class ScheduleView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# create task
class ScheduleCreate(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# shwoing detail of singel task
class ScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# delete task
class ScheduleDelete(generics.DestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Movie"))

#update task
class ScheduleUpdate(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# use to render index.html
# def home(request):
#     todos = Todo.objects.all()
#     forms = TodoForm()
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect('index')
#     return render(request, 'index.html', {'todos': todos, 'form': forms})   

# class ListTodo(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer