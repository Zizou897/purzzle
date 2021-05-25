from django.db import models
from sitewebapp.models import Convention

# Create your models here.

class Categorie(Convention):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name




class Card(Convention):
    description = models.TextField()
    categorie = models.ForeignKey("Categorie", on_delete=models.CASCADE, related_name="categorie_card")
    image = models.FileField(upload_to='image_card')

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return self.description

class CategorieWork(Convention):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'CategorieWork'
        verbose_name_plural = 'CategorieWorks'

    def __str__(self):
        return self.name


class Work(Convention):
    title = models.CharField(max_length=250)
    description = models.TextField()
    categorie = models.ForeignKey("CategorieWork", on_delete=models.CASCADE, related_name="categorie_work")
    image = models.FileField(upload_to='image_work')

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.title



class Transform(Convention):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to='image_transform')

    class Meta:
        verbose_name = 'Transform'
        verbose_name_plural = 'Transforms'

    def __str__(self):
        return self.name



class Team(Convention):
    name = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    image = models.FileField(upload_to='image_team')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name