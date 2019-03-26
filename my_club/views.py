from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "header/head.html")


def index1(request):
    return render(request, "index1.html")


def boss(request):
    return render(request, "header/bosss.html")


def administration(request):
    return render(request, "header/administration.html")


def contact(request):
    return render(request, "header/contact.html")


def history(request):
    return render(request, "header/history_club.html")

