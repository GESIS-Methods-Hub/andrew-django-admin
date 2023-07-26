from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect

from .forms import ContentForm
from .models import Content, Collection


class CollectionDetailView(DetailView):
    model = Collection


class ContentDetailView(DetailView):
    model = Content


class ContentListView(ListView):
    model = Content
    template_name = "cms/content.csv"
    content_type = "text/csv"


def add_content(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save()
            return redirect(content)

    else:
        form = ContentForm()

    return render(request, "cms/add_content.html", {"form": form})
