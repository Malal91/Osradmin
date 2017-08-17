from django.db import models
from django.contrib.auth.models import User
from randomslugfield import RandomSlugField

class Connexion(models.Model) :
    user = models.OneToOneField(User)
    
    def __str__(self):
        return self.user.username
    
class Membre(models.Model):
    user = models.OneToOneField(User)
    site_web = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    googleplus = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    signature = models.TextField(blank=True)
    pays = models.CharField(max_length=50, default=0)
    Tel = models.CharField(blank=True, max_length=50, default=0)
    langue = models.CharField(max_length=50, default=0)
    naissance = models.CharField(blank=True, max_length=100)
    #avatar = models.ImageField(blank=True, null=True, upload_to='avatars/')
    biographie = models.TextField(blank=True)
    #slug = RandomSlugField(max_length=7)
    
    def __unicode__(self):
        return self.user.username
    
class Langage(models.Model):
    langage = models.CharField(max_length=100)
    categorie = models.ForeignKey('Categorie')
    #slug = RandomSlugField(max_length=7)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.langage
    
class Categorie(models.Model):
    categorie = models.CharField(max_length=100)
    #slug = RandomSlugField(max_length=7)
    
    def __str__(self):
        return self.categorie
    
class Competence(models.Model):
    categorie = models.IntegerField()
    langage = models.IntegerField()
    niveau = models.IntegerField()
    user = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.langage
