from django.urls import path

from . import views

urlpatterns = [
    path("", views.add_content, name="add_content"),
    path("content/", views.get_all_content, name="get_all_content"),
    path("content/<int:pk>/", views.ContentDetailView.as_view(), name="show_content"),
    path("collection/", views.get_all_collection, name="get_all_collection"),
    path(
        "collection/<int:pk>/",
        views.CollectionDetailView.as_view(),
        name="show_collection",
    ),
    path(
        "collection/map/",
        views.CollectionMapListView.as_view(),
        name="get_navigation_map",
    ),
]
