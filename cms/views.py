from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ContentForm


def add_content(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save()
            return redirect(content)

    else:
        form = ContentForm()

    return render(request, "add_content.html", {"form": form})


def show_content(request, content_id):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save()
            return redirect(content)

    else:
        form = ContentForm()

    return render(request, "add_content.html", {"form": form})
