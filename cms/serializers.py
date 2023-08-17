from rest_framework import serializers

from .models import Content, Collection


class OnlyEnabledFilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(enable=True)
        return super(OnlyEnabledFilteredListSerializer, self).to_representation(data)


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["web_address", "filename"]


class OnlyEnabledContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["web_address", "filename"]
        list_serializer_class = OnlyEnabledFilteredListSerializer


class CollectionSerializer(serializers.ModelSerializer):
    content_set = OnlyEnabledContentSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = [
            "id",  # Required to resolve parent_collection
            "parent_collection",
            "title",
            "subtitle",
            "abstract",
            "cover_image",
            "content_set",
        ]
