from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {'name':'vinay','course':'python'}
    return render (request, 'index.html',context)
def about(request):
    # return HttpResponse ("this is my about page")
    return render (request, 'about.html')
def project(request):
    # return HttpResponse ("this is my project page")
    return render (request, 'project.html')
def contact(request):
    # return HttpResponse ("this is my contact page")
    return render (request, 'contact.html')
