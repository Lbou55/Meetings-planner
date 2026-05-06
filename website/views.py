from django.shortcuts import render
from meetings.models import Meeting

def home_view(request):
    context={'meetings': Meeting.objects.all()}
    return render(request, "website/home.html", context=context)

def about_view(request):
    return render(request, "website/about.html")



