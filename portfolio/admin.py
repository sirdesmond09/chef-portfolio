from django.contrib import admin
from .models import Blog, Contact, Picture

class BlogAdmin(admin.ModelAdmin):
    list_display   = ('title', 'description', 'image', 'created',)
    search_fields  = ('title', 'description')
    date_hierarchy = 'created'
    ordering       = ('created',)

class ContactAdmin(admin.ModelAdmin):
    list_display   = ('name', 'email', 'message', 'created',)
    search_fields  = ('name', 'email')
    date_hierarchy = 'created'
    ordering       = ('created',)

class PictureAdmin(admin.ModelAdmin):
    list_display   = ('author', 'chef', 'logo', 'header', 'uploaded',)
    date_hierarchy = 'uploaded'
    ordering       = ('uploaded',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Picture, PictureAdmin)