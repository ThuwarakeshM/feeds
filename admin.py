from django.contrib import admin

from .models import Category, Post, Section


class SectionInline(admin.StackedInline):
    model = Section
    extra = 3


class PostAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Section)
