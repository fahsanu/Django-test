from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.ListTodoView.as_view(), name='todos'),
    # view all tasks
    path('view/', views.ScheduleView.as_view(), name='viewS'),
    # view indiv task
    path('view/<int:pk>/', views.ScheduleDetailView.as_view(), name='viewS'),
    # create task
    path('create/', views.ScheduleCreate.as_view(), name='createS'),
    # delete task
    path('delete/<int:pk>/', views.ScheduleDelete.as_view(), name='deleteS'),   
    # update task
    path('update/<int:pk>/', views.ScheduleUpdate.as_view(), name='updateS'),


    # path('', views.home, name='home'),
    # path('', views.ListTodo.as_view()),
    # path('<int:pk>/', views.DetailTodo.as_view()),
]