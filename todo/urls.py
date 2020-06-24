
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addTodo, name='add'),
    path('complete<todo_id>/', views.completeTodo, name='complete'),
    path('completenew/<todo_id>/', views.completeTodoNew, name='completenew'),

    path('deletecomplete/', views.deleteCompleted, name='deletecomplete'),
    path('deletecompletenew/', views.deleteCompletedNew, name='deletecompletenew'),

    path('deleteall/', views.deleteAll, name='deleteall'),
    path('deleteallnew/', views.deleteAllNew, name='deleteallnew'),

    path('new/', views.home, name='new'),
    path('addnew/', views.addTodoNew, name='addnew'),


]
