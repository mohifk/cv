from django.shortcuts import render


def home_page_view(request):
    return render(request ,'cv-temp/index.html')
def language(request):
    return render(request ,'cv-temp/language.html')
def education(request):
    return render(request ,'cv-temp/education.html')
def abilites(request):
    return render(request ,'cv-temp/abilites.html')
def projects(request):
    return render(request ,'cv-temp/projects.html')
def contects_bio(request):
    return render(request ,'cv-temp/contects_bio.html')


# Create your views here.
