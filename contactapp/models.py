from django.db import models
from sitewebapp.models import Convention
# Create your models here.


class Contact(Convention):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    subject = models.TextField()
    message = models.TextField()


    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return  self.name

    

class Newsletter(Convention):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return  self.email



class CreateSucce(Convention):
    title = models.CharField(max_length=50)
    sous_title = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        verbose_name = 'CreateSucce'
        verbose_name_plural = 'CreateSucces'

    def __str__(self):
        return  self.title



class Social(Convention):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    link = models.URLField()
    

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

    def __str__(self):
        return  self.name

    


class Assitance(Convention):
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    

    class Meta:
        verbose_name = 'Assitance'
        verbose_name_plural = 'Assitances'

    def __str__(self):
        return  self.name



class Pack(Convention):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    period = models.CharField(max_length=255)
    activate = models.BooleanField(default=False)

    class Meta():
        verbose_name = 'Pack'
        verbose_name_plural = 'Packs'

    def __str__(self):
        return self.title

class Advantage(Convention):
    label = models.CharField(max_length=255)
    label_activate = models.BooleanField(default=True)
    pack = models.ManyToManyField("contactapp.Pack", related_name="advantage_pack")

    class Meta():
        verbose_name = 'Advantage'
        verbose_name_plural = 'Advantages'

    def __str__(self):
        return self.label