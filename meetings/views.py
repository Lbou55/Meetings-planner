from django.shortcuts import render, redirect
from meetings.models import Meeting, Room
from meetings.forms import MeetingForm

def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("website:home")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})