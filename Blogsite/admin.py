from django.contrib import admin
from .models import Blog, BlogUser, Contact


class BlogUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'username']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['user', 'uploaded_on']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(BlogUser, BlogUserAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
