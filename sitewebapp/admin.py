from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
# Register your models here.

@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title',)





@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('image',)




@admin.register(models.BannerAbout)
class BannerAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_view', 'date_add','status')

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:200px; height:100px">')



@admin.register(models.BannerWork)
class BannerWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'sous_title', 'image', 'date_add', 'status')




@admin.register(models.BannerContact)
class BannerContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'sous_title', 'date_add', 'image')





@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'sous_title', 'date_add', 'icon')




@admin.register(models.But)
class ButAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_add', 'icon')




@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'date_add', 'status')

    

@admin.register(models.Choose)
class ChooseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_add', 'status')



@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name_site', 'email','phone','copyright', 'date_add', 'status')

