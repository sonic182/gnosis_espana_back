from django.contrib import admin
from news.models import Post, Draft, Category, Tag
from django.forms.models import model_to_dict


class CategoryInline(admin.StackedInline):
    model = Category
    min_num = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'see_categories', 'see_tags', 'created_at', 'updated_at']
    list_filter = ['active', 'created_at', 'updated_at']

def publish_draft(modeladmin, request, queryset):
    for draft in queryset:
        item = model_to_dict(draft)
        item.pop('id', None)
        categories = item.pop('categories', None)
        tags = item.pop('tags', None)
        p = Post(**{**item, 'active': True})
        p.save()
        for category in categories:
            p.categories.add(category)
        for tag in tags:
            p.tags.add(tag)
        draft.delete()

publish_draft.short_description = "Publica los borradores seleccionados"

@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = ['title', 'see_categories', 'see_tags', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    actions = [publish_draft]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
