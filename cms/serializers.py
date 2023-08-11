from rest_framework import serializers

from .models import Affiliation, Author, Content, Collection


class AffiliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliation
        fields = ["name", "department", "city", "country", "url"]


class AuthorSerializer(serializers.ModelSerializer):
    affiliation = AffiliationSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "orcid", "url", "affiliation"]


class OnlyEnabledFilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(enable=True)
        return super(OnlyEnabledFilteredListSerializer, self).to_representation(data)


class ContentWithAuthorSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = ["git_repository", "filename", "author"]


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["git_repository", "filename", "author"]


class OnlyEnabledContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["git_repository", "filename"]
        list_serializer_class = OnlyEnabledFilteredListSerializer


class CollectionSerializer(serializers.ModelSerializer):
    content_set = OnlyEnabledContentSerializer(many=True, read_only=True)

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
