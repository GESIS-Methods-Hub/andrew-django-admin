from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("content", views.ContentViewSet)
router.register("collection", views.CollectionViewSet)

urlpatterns = [
    path("", views.add_content, name="add_content"),
    path("api/", include(router.urls)),
    path("content/<int:pk>/", views.ContentDetailView.as_view(), name="show_content"),
    path(
        "collection/<int:pk>/",
        views.CollectionDetailView.as_view(),
        name="show_collection",
    ),
]
