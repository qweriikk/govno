from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

site = admin.site

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_filter = ['date_posted']
    search_fields = [
        'title__icontains',
    ]
    readonly_fields = ['get_image', 'id']
    
    @admin.display(description='Изображение', empty_value='---')
    def get_image(self, model_object):
        if model_object and model_object.image:
            return mark_safe(f'<img src="{model_object.image.url}">')
