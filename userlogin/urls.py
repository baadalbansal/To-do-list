from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView 

from userlogin.views import TaskCreate, TaskDeleteView, TaskDetail, TaskList, TaskUpdate, login
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('task', TaskList.as_view(), name="tasks"),
    path('task/task-create/', TaskCreate.as_view(), name="task-create"),
    path('task/task-delete/<int:pk>/', TaskDeleteView.as_view(), name="task-delete"),
    path('task/task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task"),
    path('login', views.login, name="login"),
    path('logout', LogoutView.as_view(next_page="login"), name="logout"),
    # we have taken care of logout function using class based view = LogoutView 
    path('signup', views.signup, name="signup"),
]
