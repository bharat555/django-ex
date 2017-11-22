from django.contrib import admin
#hello
from .models import PageView

# Register your models here.


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)
