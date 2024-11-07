from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contacts.html")
def blogs(request):
    return render(request, "Blogs.html")
def services(request):
    return render(request, "Services.html")

