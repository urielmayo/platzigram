from django.contrib import admin

from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    #display list
    list_display = (
        'pk',
        'user',
        'title',
        'profile',
        'photo'
    )

    list_display_links = (
        'pk',
        'user',
        'profile',
    )

    list_editable = (
        'title',
        'photo',
    )
