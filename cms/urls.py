from django.urls import path

from . import views

urlpatterns = [
    path("", views.add_content, name="add_content"),
    path("content/", views.ContentListView.as_view(), name="get_all_content"),
    path("content/<int:pk>/", views.ContentDetailView.as_view(), name="show_content"),
    path(
        "collection/<int:pk>/",
        views.CollectionDetailView.as_view(),
        name="show_collection",
    ),
]
