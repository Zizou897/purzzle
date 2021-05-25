from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

# Register your models here.

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add', 'status')
    


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('description', 'image_view','date_add', 'status')

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:200px; height:100px">')
    image_view.short_description = "Aperçu d'images"
    


@admin.register(models.CategorieWork)
class CategorieWorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add', 'status')
    


@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_view','date_add', 'status')

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:200px; height:100px">')
    image_view.short_description = "Aperçu d'images"
    



@admin.register(models.Transform)
class TransformAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_view','date_add', 'status')

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:200px; height:100px">')
    image_view.short_description = "Aperçu d'images"

  

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','job', 'image_view','date_add', 'status')

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:200px; height:100px">')
    image_view.short_description = "Aperçu d'images"
    