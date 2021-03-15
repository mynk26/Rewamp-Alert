from django.urls import path
from .views import Dashboard, AddnewView, TodoView, AlltaskView
urlpatterns = [
    path('',Dashboard.as_view(),name='Dashboard'),
    path('addnew/',AddnewView.as_view(),name='AddNewView'),
    path('todo/',TodoView.as_view(),name='ToDoView'),
    path('alltask/',AlltaskView.as_view(),name='AlltaskView')
]