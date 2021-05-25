
from django.shortcuts import render,get_object_or_404
from contactapp import models as models_contact
from portfolioapp import models as models_portfolio
from . import models
# Create your views here.


def index(request):
    socials = models_contact.Social.objects.filter(status=True)
    services = models.Service.objects.filter(status=True).first()
    sites = models.Website.objects.filter(status=True).first()
    sliders = models.Slider.objects.filter(status=True)
    works = models_portfolio.Work.objects.filter(status=True).order_by('-date_add')[:6]
    return render(request, 'index.html', locals())




def about(request):
    bannerAbouts = models.BannerAbout.objects.filter(status=True).first()
    socials = models_contact.Social.objects.filter(status=True)
    teams = models_portfolio.Team.objects.filter(status=True)
    partners = models.Partner.objects.filter(status=True)
    chooses = models.Choose.objects.filter(status=True).first()
    sites = models.Website.objects.filter(status=True).first()
    buts = models.But.objects.filter(status=True)
    return render(request, 'about.html', locals())




def contact(request):
    bannerContacts = models.BannerContact.objects.filter(status=True).first()
    creates = models_contact.CreateSucce.objects.filter(status=True).first()
    assistences = models_contact.Assitance.objects.filter(status=True)
    socials = models_contact.Social.objects.filter(status=True)
    sites = models.Website.objects.filter(status=True).first()
    return render(request, 'contact.html', locals())




def pricing(request):
    advantages = models_contact.Advantage.objects.filter(status=True)
    packs = models_contact.Pack.objects.filter(status=True)
    socials = models_contact.Social.objects.filter(status=True)
    sites = models.Website.objects.filter(status=True).first()
    return render(request, 'pricing.html', locals())




def work(request):
    categorieWorks = models_portfolio.CategorieWork.objects.filter(status=True)
    transforms = models_portfolio.Transform.objects.filter(status=True)
    works = models_portfolio.Work.objects.filter(status=True)
    socials = models_contact.Social.objects.filter(status=True)
    sites = models.Website.objects.filter(status=True).first()
    return render(request, 'work.html', locals())




def work_single(request, id):
    socials = models_contact.Social.objects.filter(status=True)
    sites = models.Website.objects.filter(status=True).first()
    worksid = get_object_or_404(models_portfolio.Work, id=id)
    return render(request, 'work-single.html', locals())
