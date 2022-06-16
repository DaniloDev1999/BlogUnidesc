from django.contrib import admin
from . models import post
# Register your models here.
@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = "titulo","slug","autor","criado","atualizado"
    prepopulated_fields = {"slug":("titulo",)}