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
        upload = request.POST.get('myfile')
        print(f"Ticket=> Category: {category} and Description: {description} and upload {upload}")
        if category and description:
            ticket = Ticket.objects.create(category=category, description=description, upload=upload)
            ticket.save()
            return redirect("index")
    return HttpResponse("Not submiited..")


from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def generate_certificate(request):
    # Hard-coded student and course data
    student_name = "John Doe"
    course_name = "Introduction to Django"
    completion_date = "August 23, 2024"

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

    # Create the PDF object, using the HttpResponse object as its "file."
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Sample style sheet
    styles = getSampleStyleSheet()
    flowables = []

    # Certificate title
    title = Paragraph("Certificate of Completion", styles['Title'])
    flowables.append(title)

    # Spacer between elements
    flowables.append(Spacer(1, 50))

    # Student Name
    student_para = Paragraph(f"This is to certify that <b>{student_name}</b>", styles['Normal'])
    flowables.append(student_para)

    # Course Name
    course_para = Paragraph(f"has successfully completed the course <b>{course_name}</b>", styles['Normal'])
    flowables.append(course_para)

    # Completion Date
    date_para = Paragraph(f"on <b>{completion_date}</b>", styles['Normal'])
    flowables.append(date_para)

    # Spacer before signature line
    flowables.append(Spacer(1, 50))

    # Signature Line
    signature_line = Paragraph("______________________________", styles['Normal'])
    flowables.append(signature_line)
    signature_label = Paragraph("Instructor's Signature", styles['Normal'])
    flowables.append(signature_label)

    # Build the PDF
    doc.build(flowables)

    return response






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