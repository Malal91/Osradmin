from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Connexion, Membre, Categorie, Langage
from .forms import ConnexionForm, MembreForm, CategorieForm, LangageForm

def connexion(request):
    error = False
    
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user :
                login(request, user)
            else :
                error = True
    else :
        form = ConnexionForm()
    
    return render(request, 'osradmin/login.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

class NotificationView(TemplateView):
    def get(self, request, *args, **kwargs):
        id_user = request.GET['id']
        user = Membre.objects.filter(id=id_user)
        data = serializers.serialize('json', user, fields=('site_web'))
        return HttpResponse(data, content_type='application/json')

#@cache_page(60 * 15)
@login_required
def userAdd(request):
    error = False
    
    if request.method == "POST":
        form = MembreForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            site_web = form.cleaned_data['site_web']
            facebook = form.cleaned_data['facebook']
            twitter = form.cleaned_data['twitter']
            instagram = form.cleaned_data['instagram']
            linkedin = form.cleaned_data['linkedin']
            googleplus = form.cleaned_data['google_plus']
            signature = form.cleaned_data['signature']
            biographie = form.cleaned_data['biographie']
            password = User.objects.make_random_password() #Nous generons automatiquement le mot de passe du membre (système offert par django)
            user = User.objects.create_user(username, email, password) # Nous créons le membre avec les trois premièrs paramètres
            user.first_name, user.last_name = first_name, last_name # Et là nous ajoutons les autres paramètres
            membre = Membre(user=user, site_web=site_web, facebook=facebook, twitter=twitter, instagram=instagram, linkedin=linkedin, googleplus=googleplus, signature=signature, biographie=biographie) # Et là enregistrement de tous les informations du membre dans la base de données dans la table 'Membre' c'est-à-dire le model 'Membre'(chaque model represente une table dans la base de donnée)
            membre.save()
            
            error = True
    else:
        form = MembreForm()
        
    return render(request, 'osradmin/user_add.html', locals())

#@cache_page(60 * 15)
@login_required
def userlist(request):
    membre = Membre.objects.order_by("-user_id")
    return render(request, 'osradmin/user_list.html', locals())

#@cache_page(60 * 15)
@login_required
def addCategorie(request):
    right = False
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            categorie_name = form.cleaned_data['categorie']
            categorie = Categorie(categorie=categorie_name)
            categorie.save()
            
            right = True
    else:
        form = CategorieForm()
            
    return render(request, 'osradmin/categorie_add.html', locals())

#@cache_page(60 * 15)
@login_required
def addLangage(request):
    right = False
    if request.method == "POST":
        form = LangageForm(request.POST)
        if form.is_valid():
            langage_name = form.cleaned_data['langage']
            categorie = form.cleaned_data['categorie']
            langage = Langage(langage=langage_name, categorie=categorie)
            langage.save()
            
            right = True
    else:
        form = LangageForm()
        
    return render(request, 'osradmin/add_langage.html', locals())