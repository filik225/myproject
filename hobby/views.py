
from django.shortcuts import render


def home(request):
    context = {
        "hobby_name": "Programowanie",
        "description": "Lubię tworzyć aplikacje i poznawać nowe technologie.",
    }
    return render(request, "hobby/home.html", context)


def about(request):
    context = {
        "hobby_name": "Programowanie",
    }
    return render(request, "hobby/about.html", context)


def gallery(request):
    return render(request, "hobby/gallery.html")
