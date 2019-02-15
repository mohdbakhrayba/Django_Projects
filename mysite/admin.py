from django.contrib import admin

from .models import Page , Category , Comment

class PageAdmin(admin.ModelAdmin):
    model = Page
    filter_horizontal = ('categories',)

admin.site.register(Page, PageAdmin)

admin.site.register(Category)

admin.site.register(Comment)