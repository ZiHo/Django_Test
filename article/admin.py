from django.contrib import admin
from .models import Ariticle


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content")


admin.site.register(Ariticle, ArticleAdmin)
