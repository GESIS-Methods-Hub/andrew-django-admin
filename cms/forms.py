from django.forms import ModelForm
from .models import Content


class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ["git_repository", "file", "collection", "group"]
