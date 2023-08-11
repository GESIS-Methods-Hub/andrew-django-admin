from django.contrib import admin

from .models import Affiliation, Author, Collection, Content

admin.site.register(Affiliation)
admin.site.register(Author)
admin.site.register(Collection)
admin.site.register(Content)
