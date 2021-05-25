from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'status')


@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_add', 'status')




@admin.register(models.CreateSucce)
class CreateSucceAdmin(admin.ModelAdmin):
    list_display = ('title', 'sous_title', 'date_add', 'status')



@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'date_add', 'status')
    



@admin.register(models.Assitance)
class AssitanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'phone', 'icon', 'date_add', 'status')
    


@admin.register(models.Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'period','activate', 'date_add', 'status')
    



@admin.register(models.Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('label', 'label_activate', 'date_add', 'status')
    
    
