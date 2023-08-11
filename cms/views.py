from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions

from .forms import ContentForm
from .models import Content, Collection
from .serializers import ContentSerializer, CollectionSerializer


class ContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Content.objects.filter(enable=True)
    serializer_class = ContentSerializer
    permission_classes = [permissions.AllowAny]


class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.AllowAny]


class CollectionDetailView(DetailView):
    model = Collection


class ContentDetailView(DetailView):
    model = Content


def add_content(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save()
            return redirect(content)

    else:
        form = ContentForm()
        form.fields["collection"].queryset = Collection.objects.filter(
            parent_collection__isnull=False
        )

    return render(request, "cms/add_content.html", {"form": form})
