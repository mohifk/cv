from django.shortcuts import render
import requests
import os
def home_page_view(request):
    return render(request ,'.\cv-temp\index.html')
def language(request):
    return render(request ,'.\cv-temp\language.html')
def education(request):
    return render(request ,'.\cv-temp\education.html')
def abilites(request):
    return render(request ,'.\cv-temp\\abilites.html')
def projects(request):
    return render(request ,'.\cv-temp\projects.html')
def contects_bio(request):
    return render(request ,'.\cv-temp\contects_bio.html')
# Create your views here.
def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
def index(request):
    times = int(os.environ.get('TIMES', 3))
    return HttpResponse('Hello! ' * times)
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

