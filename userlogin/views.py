from asyncio import tasks
from pyexpat import model
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login 
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


# Create your views here.
def login(request):
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username , password = password)
        from django.contrib.auth import  login
        login(request,user)
        messages.success(request, 'User logged in.')
        redirect("/")

    return render(request,'userlogin/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]


        myuser = User.objects.create_user(username,email,pass1)
        myuser.firstname = firstname
        myuser.lastname = lastname
        myuser.save()
        user = authenticate(username=username , password = pass1)
        from django.contrib.auth import  login
        login(request,user)
        
        return redirect('/')


    return render(request,'userlogin/signup.html')

def homepage(request):
    return render(request,'userlogin/index.html') 



class TaskList(ListView):
    model = Task      
    context_object_name = "tasks"
    #as default listview look for templatefile modelname_list.html but we can also override it by adding template_name=""
   
    # default of context_list_object  in list view is object_list  but we can change it as well (look in template file)
    

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    #as default listview look for templatefile modelname_detail.html but we can also override it by adding template_name=""

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    #as default listview look for templatefile modelname_form.html but we can also override it by adding template_name=""
    #success_ulr is used because after its success it redirect to tasks
    #by default create view makes a form and we use that by writing {{form.as_p}} in the form tag in template and we add .as_p for as paragraph otherwise all fields come in  same line

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    #by default the context_object_name is object
    success_url = reverse_lazy("tasks")

    # By default DeleteView look’s for a template with the prefix of the model name (task) and the suffix of _confirm_delete.html if not otherwise set (task_confirm_delete.html). This can be overridden by setting the “template_name” attribute.



    