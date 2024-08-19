from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from .models import *


def index(request):
    page_name = "Home page"
    # Extract the choices from the model
    categories = Ticket.possible_issues
    print("Categoris:", categories)
    return render(request, "home.html", {'page_name': page_name, 'categories':categories})

def create_ticket(request):
    if request.method == "POST":
        category = request.POST.get('category')
        description = request.POST.get('description')
        print(f"Ticket=> Category: {category} and Description: {description}")
        if category and description:
            ticket = Ticket.objects.create(category=category, description=description)
            ticket.save()
            return redirect("index")
    return HttpResponse("Not submiited..")


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