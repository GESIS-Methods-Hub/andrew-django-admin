from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("collection", views.CollectionViewSet)

urlpatterns = [
    path("", views.add_content, name="add_content"),
    path("api/", include(router.urls)),
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
