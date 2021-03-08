from django.urls import path
from .views import IndexView,LoginView,SignupView, LogoutView
urlpatterns = [
    path('',IndexView.as_view()),
    path('login/',LoginView.as_view()),
    path('signup/',SignupView.as_view()),
    path('logout/',LogoutView.as_view()),
]