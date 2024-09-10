from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import *

# built in function for sending messages in django
from django.contrib import messages

# built in django user
from django.contrib.auth.models import User

# for user login
from django.contrib.auth import authenticate, login, logout

# check to make the user is login before acccessing the view
from django.contrib.auth.decorators import login_required

# imported the send mail function from send_mail.py
from .send_mail import send_email

# for sending request of of the django app or python 
import requests

from django.http import JsonResponse
from user_agents import parse
from datetime import datetime

def index(request):
    page_name = "Home page"
    # Extract the choices from the model
    categories = Ticket.possible_issues
    print("Categoris:", categories)
    return render(request, "home.html", {'page_name': page_name, 'categories':categories})

def time():
    # Get the current date and time
    now = datetime.now()

    # Format it to display day, month, year, and time
    formatted_time = now.strftime("%d %B %Y, %H:%M:%S")
    return formatted_time


def get_ip_from_ipify():
    try:
        # Make a request to ipify API to get the public IP
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json().get('ip')
        return ip
    except Exception as e:
        return f"Error: {str(e)}"

def get_client_info(request):
    # Get public IP address from ipify
    ip = get_ip_from_ipify()

    # Get browser and device information
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    user_agent_info = parse(user_agent)
    
    browser = f"{user_agent_info.browser.family} {user_agent_info.browser.version_string}"
    os = f"{user_agent_info.os.family} {user_agent_info.os.version_string}"
    device = user_agent_info.device.family

    # Return the data as a JSON response
    return {
        'ip': ip,
        'browser': browser,
        'os': os,
        'device': device
    }




def create_ticket(request):
    if request.method == "POST":
        category = request.POST.get('category')
        description = request.POST.get('description')
        upload = request.POST.get('myfile')
        print(f"Ticket=> Category: {category} and Description: {description} and upload {upload}")
        if category and description:
            ticket = Ticket.objects.create(category=category, description=description, upload=upload)
            ticket.save()
            return redirect("index")
    return HttpResponse("Not submiited..")

@login_required
def dashboard(request):
    page_name = "Dashboard page"
    # Extract the choices from the model
    tickets = Ticket.objects.all()
    print("Categoris:", tickets)
    return render(request, "dashboard.html", {'page_name': page_name, 'tickets':tickets})


def user_login(request):
    page_name = "login page"

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                subject = "Login Successfull"
                body = f"A Succesfully login from {get_client_info(request)} at {time()}"
                send_email(subject, body, user.email, "abibangbrandon855@outlook.com", "Devops23#A_")
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Please enter both username and password')

    return render(request, "login.html", {'page_name': page_name})



def register(request):
    page_name = "Register page"
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if(username and password and email):
            user = User.objects.create(username=username, password=password, email=email)
            user.set_password(password)
            user.save()
            subject = "Welcome to the ticketing system"
            body = "Hello, welcome to the ticketing system. You have successfully registered"
            send_email(subject, body, email, "abibangbrandon855@outlook.com", "Devops23#A_")
            
            return redirect("login")
        else:
            messages.error(request, 'An error occured..')
            
    return render(request, "register.html", {'page_name': page_name})

def user_logout(request):
    logout(request)
    return redirect("index")
    
# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         author = request.POST.get('Aname')
#         if title and content and author:
#             post = Post.objects.create(title=title, content=content,author=author, published_date=timezone.now())
#             post.save()
#             return redirect('home')
        
#     return render(request, "add_post.html")



