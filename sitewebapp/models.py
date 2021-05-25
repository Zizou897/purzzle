from django.db import models

# Create your models here.

class Convention(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    class Meta:
        abstract = True


class Slider(Convention):
    title = models.CharField(max_length=250)
    description = models.TextField()
    plus = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
    
    def __str__(self):
        return self.title
        



class Banner(Convention):
    image = models.FileField(upload_to='image_banner')

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    
    def __str__(self):
        return self.title
        



class BannerAbout(Convention):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to='image_about')

    class Meta:
        verbose_name = 'BannerAbout'
        verbose_name_plural = 'BannerAbouts'
    
    def __str__(self):
        return self.title
        



class BannerWork(Convention):
    title = models.CharField(max_length=50)
    sous_title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(upload_to='image_work')

    class Meta:
        verbose_name = 'BannerWork'
        verbose_name_plural = 'BannerWorks'
    
    def __str__(self):
        return self.title



class BannerContact(Convention):
    title = models.CharField(max_length=50)
    sous_title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(upload_to='image_contact')

    class Meta:
        verbose_name = 'BannerContact'
        verbose_name_plural = 'BannerContacts'
    
    def __str__(self):
        return self.title



class Service(Convention):
    title = models.CharField(max_length=250)
    sous_title = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.title


class But(Convention):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'But'
        verbose_name_plural = 'Buts'
    
    def __str__(self):
        return self.title



class Partner(Convention):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
    
    def __str__(self):
        return self.title



class Choose(Convention):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to='image_choose')

    class Meta:
        verbose_name = 'Choose'
        verbose_name_plural = 'Chooses'
    
    def __str__(self):
        return self.title


class Website(Convention):
    phone = models.CharField(max_length=250)
    copyright = models.CharField(max_length=250)
    name_site = models.CharField( max_length=250)
    email = models.EmailField()
    description_team = models.TextField()
    description_footer = models.TextField()
    description_creative = models.TextField()
    description_transform = models.TextField()
    description_newsletter = models.TextField()

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

        def __str__(self):
            return self.name_site

