from rest_framework import serializers

from .models import Content, Collection


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["git_repository", "filename"]


class CollectionSerializer(serializers.ModelSerializer):
    content_set = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = [
            "parent_collection",
            "title",
            "subtitle",
            "abstract",
            "cover_image",
            "content_set",
        ]
