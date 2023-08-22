from django.contrib import admin

from .models import Collection, Content


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "abstract")
    list_filter = ("parent_collection", )


@admin.action(description='Enable Content',)
def enable_content(modeladmin, request, queryset):
    queryset.update(enable = True)
    
@admin.action(description='Disable Content',)
def diseble_content(modeladmin, request, queryset):
   queryset.update(enable = False)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("web_address", "filename", "enable")
    list_filter = ("enable", "collection", )

    actions = (enable_content, diseble_content)
