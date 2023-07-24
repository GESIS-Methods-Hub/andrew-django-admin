from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContentForm


def add_content(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    else:
        form = ContentForm()

    return render(request, "add_content.html", {"form": form})
