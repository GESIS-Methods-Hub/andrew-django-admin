from django.urls import path

from . import views

urlpatterns = [
    path("", views.add_content, name="add_content"),
    path("content/<int:content_id>/", views.show_content, name="show_content"),
    path(
        "collection/<int:collection_id>/", views.show_collection, name="show_collection"
    ),
]
