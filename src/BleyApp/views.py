import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import LeyssareMembres, VersementLeyssare, LeyssareCaisse, LeyssareDepenses, VersionPeriodique
from django.db.models import Q
from .forms import FormUserMembres, Authentification, MyUserForm, MyForm
from faker import Faker
# Create your views here.
def base(request):
    return  render(request, 'leyssare/Accueil.html')
def index(request):
    return render(request, 'leyssare/index.html')


def accueil(request):
    return render(request, 'leyssare/Accueil.html')


def membres(request):
    return render(request, 'leyssare/Membres.html')

def versees(request):
    return render(request, 'leyssare/Ont-verses.html')

def admin_auth(request):
    context = {'context':'Bienvenue sur la page de authentification.'}
    return render(request, 'leyssare/leyadmin/admin_auth.html', context)

def tresorerie(request):
    return render(request, 'leyssare/Tresorerie.html')


def propos(request):
    return render(request, 'leyssare/À-propos-de.html')


def liste_membres(request):
    if request.method == 'GET':
        membres = LeyssareMembres.objects.all()
        context = {'data':membres}
        return render(request, 'leyssare/liste_membres.html', context)

def membres_ont_versees(request):
    if request.method == 'GET':
        ont_versees = VersementLeyssare.objects.all() # à revoir le filtre ici
        print(ont_versees)

        context = {'data': ont_versees}
        return render(request, 'leyssare/membre_qui_ont_versees.html', context)

def depensee(request):
    depence = LeyssareCaisse.objects.all()
    context = {'data':depence}
    return render(request, 'leyssare/depencee.html', context)

def total_depense(request):
    depence = LeyssareCaisse.objects.all()
    total = 0
    for items in depence:
        total += items.montant_depencee
        print(total)
    context={'data':total}
    return render(request, 'leyssare/total_depense.html', context)


def capital_restante(request):
    capital_restante = LeyssareCaisse.objects.all()
    total_somme_depensee = 0
    for items in capital_restante:
        total_somme_depensee += items.montant_depencee

    #Ici on recupère le dernier montant disponible
    dernier_montant_dispo = LeyssareCaisse.objects.last().montant_fg_dispo

    total_restante = dernier_montant_dispo - total_somme_depensee

    context = {'data': total_restante}
    return render(request, 'leyssare/capital_restante.html', context)
#On ajoute ici la somme versée au somme total disponible dans la caisse
def gestion_caisse(request):
    #ici, on recupère le dernier montant qu'un membres viens de cotisé
    recup_versement_cfa = VersementLeyssare.objects.exclude(montant_cfa=None).latest('id').montant_cfa
    recup_versement_fg = VersementLeyssare.objects.exclude(montant_fg=None).latest('id').montant_fg

    #ici, on recupére le dernier montant depensées
    recup_depense = LeyssareDepenses.objects.latest('id').montant_depensee
    print(recup_versement_cfa)

    #On ajoute la somme qu'un membre viens de cotisé, à notre caisse LeyssareCaisse

    data_cfa = LeyssareCaisse.objects.last().montant_cfa_dispo
    data_fg = LeyssareCaisse.objects.last().montant_fg_dispo

    #ajout d'une depense sortie dans le Caisse
    data_depense = LeyssareCaisse.objects.last().montant_depencee

    ajout_cfa = recup_versement_cfa + data_cfa
    ajout_fg = recup_versement_fg + data_fg

    ajout_depense = recup_depense + data_depense

    obj = LeyssareCaisse.objects.get(pk=5)
    obj.montant_cfa_dispo = ajout_cfa
    obj.montant_fg_dispo = ajout_fg
    obj.montant_depencee = ajout_depense
    obj.save()

    return HttpResponse(f'<h2>Montant CFA:{obj.montant_cfa_dispo}</br>'
                        f'Montant FG: {obj.montant_fg_dispo} '
                        f'</br> Montant depensée: {obj.montant_depencee} </h2>')
def etat_de_caisse(request):
    obj = LeyssareCaisse.objects.all()
    context={'data':obj}
    return render(request, 'leyssare/etat_caisse.html', context)
def user_has_cotise(request):
    recup_user = VersementLeyssare.objects.last()
    print(recup_user.prenom)
    user = recup_user.versionperiodique_set.all()


    return HttpResponse(f'<h2> Username : </h2>')


def auth_user(request, urls, urls_param):
    print(urls, urls_param)
    if request.method == 'POST':
        form = Authentification(request.POST)
        number = request.POST.get('id_number')
        ont_versees = LeyssareMembres.objects.only('id_number')

        id_saved = []
        prenoms = []
        for i in ont_versees:
            #on remplit les deux tableaux, l'ID_number et le prenom
            id_saved.append(i.id_number)
            prenoms.append(i.prenom)
        print(id_saved)
        #Ici, on vérifie si l'ID_number que l'utilsateur à taper se trouve dans la base de données
        if number in id_saved:
            #On récupère l'index qui correspond à notre tableau ID_number
            recup_index = id_saved.index(number)
            print(f'{recup_index}, est le index ')
            #On récupère ici l'index numéro recup_index de notre tableau prenoms[]
            user = prenoms[recup_index]
            print(user)
            if urls.endswith('page_membres') or (urls.count('/page_membres/auth_page') >= 1):
                print(urls.count('/page_membres/auth_page') >= 1)
                membres = LeyssareMembres.objects.all()
                context = {'data': membres,
                           'user':user}

                return render(request, 'leyssare/liste_membres.html', context)
            elif urls.endswith('membres_ont_versees') or urls.count('/membres_ont_versees/auth_page') >= 1:
                ont_versees = VersementLeyssare.objects.all()  # à revoir le filtre ici
                print(ont_versees)
                context = {'data': ont_versees,
                           'user':user}
                return render(request, 'leyssare/membre_qui_ont_versees.html', context)
            elif urls.endswith('depensee') or (urls.count('/depensee/auth_page') >= 1):
                obj = LeyssareCaisse.objects.all()
                context = {'data': obj,
                           'user':user}
                print(f'{urls}/{urls_param}')
                return render(request, 'leyssare/etat_caisse.html', context)
            elif urls.endswith('depense_accumule') or (urls.count('/depense_accumule/auth_page')):
                obj = LeyssareCaisse.objects.all()
                context = {'data': obj,
                           'user':user}
                print(f'{urls}/{urls_param}')
                return render(request, 'leyssare/depencee.html', context)
            elif urls.endswith('capital_restant') or (urls.count('/capital_restant/auth_page')):
                capital_restante = LeyssareCaisse.objects.all()
                total_somme_depensee = 0
                for items in capital_restante:
                    total_somme_depensee += items.montant_depencee

                # Ici, on récupère le dernier montant disponible
                dernier_montant_dispo = LeyssareCaisse.objects.last().montant_fg_dispo

                total_restante = dernier_montant_dispo - total_somme_depensee

                context = {'data': total_restante,
                           'user':user}
                return render(request, 'leyssare/capital_restante.html', context)
            elif urls.endswith('total_depense') or (urls.count('/total_depense/auth_page')):
                print(f'{urls}/{urls_param}')
                depence = LeyssareCaisse.objects.all()
                total = 0
                for items in depence:
                    total += items.montant_depencee
                    print(total)
                context = {'data': total,
                           'user':user}
                return render(request, 'leyssare/total_depense.html', context)

            else:
                return HttpResponse('<p>Nous ne connaissons pas l\'url visité</p>')
        else:
            form = Authentification(initial={'id_number':''})
            context = {'error':number,
                       'form':form}
            return render(request, 'leyssare/auth_page.html', context)
    else:
        form = Authentification()
    return render(request,'leyssare/auth_page.html', {'form':form})

def create_account(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        mail = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = f"Hello {username}"
        print('Your account is create with succes')
        return render(request, 'leyssare/leyadmin/create_admin.html', {'user': user})
    else:
        form = MyForm()
        return render(request, 'leyssare/leyadmin/create_admin.html', {'form':form})

#home admin
def admin_index(request):
    return render(request, 'leyssare/leyadmin/adminbase.html')

#'''Gestion d'administration'''
def admin_connexion(request):
    form = MyUserForm()
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('pass_word')
        #On verifie si l'utilsateur exist
        if User.objects.filter(username=username).exists():
            #Et si il est authetifié
            user = authenticate(username=username, password=password)
            if user is not None:
                #On connecte l'utilisateur
                login(request, user)
                print(f"L'utilisateur existe bien authentifié  {user}")
                context = {'data':f"Hello {username.upper()} You are connected in your Admin Page, you can add what you will in the Database."}
                return render(request, 'leyssare/leyadmin/admin_auth.html', context)
            else:
                print('Le mot de passe est faux.')
                context = {'error': f'This Password is fals',
                           'form':form}
                return render(request, 'registration/login.html', context)
        else:
            print("L'utilisateur n'existe pas. ")
            context = {'error': f'This user dont exists ',
                       'form':form}
            return render(request, 'registration/login.html',context)

    else:
        context = {'error':'Request type GET',
                   'message':'You must be connected before.',
                   'form':form}
        return render(request, 'registration/login.html', context)
#Deconnecter l'utilisateur
def admin_deconnexion(request):
    logout(request)
    # Redirect to a success page.
    form = MyUserForm()
    context = {'error':'You are deautheticated now. ',
               'form': form,}
    return render(request,'registration/login.html', context)
#gestion de formulaire d'inscription
@login_required(login_url='../../../BleyApp/login/')
def membres_registrer(request):
        if request.method == 'POST':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            pays = request.POST.get('pays')

            #implementation de l'ID de l'utilisateur
            fake = Faker(locale='fr')
            PERSONNAL_ID = fake.ean8(prefixes=('00',))

            usr = LeyssareMembres(nom=nom, prenom=prenom, pays=pays, id_number=PERSONNAL_ID)
            usr.save()
            print(nom, prenom, pays, PERSONNAL_ID)
            context = {'data':'Utilisateur enregistré avec succés. '}
            return render(request, 'leyssare/leyadmin/user_creation.html', context)
        else:
            return render(request, 'leyssare/leyadmin/user_creation.html')


#Gestionnaire de Versement
@login_required(login_url='../../../BleyApp/login/')
def user_versement(request):

        if request.method == 'POST':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            pays = request.POST.get('pays')
            montant_cfa = request.POST.get('montant_cfa')
            montant_fg = request.POST.get('montant_fgn')

            #Ici, on vérifie si la nature de somme cotisé est FCFA
            if montant_fg == '':
                montant_fg = None
                if montant_cfa.isdigit():
                    montant_cfa = int(montant_cfa)
                    recup = LeyssareCaisse.objects.all()
                    for data_recup in recup:
                        #On ajoute cette somme à notre caisse LeyssareCaisse
                        data_recup.montant_cfa_dispo += montant_cfa
                        data_recup.save()
                        print(data_recup.montant_cfa_dispo)
                else:
                    context = {'error2': 'Ce Champs doit être de type monnaie FCFA.'}
                    return render(request, 'leyssare/leyadmin/user_cotisation.html', context)

            # Ici, on vérifie si la nature de somme cotisé est FGN
            elif montant_cfa == '':
                montant_cfa = None
                if montant_fg.isdigit():
                    montant_fg = int(montant_fg)
                    recup = LeyssareCaisse.objects.all()
                    for data_recup in recup:
                        # On ajoute cette somme à notre caisse LeyssareCaisse
                        data_recup.montant_fg_dispo += montant_fg
                        data_recup.save()
                        print(data_recup.montant_fg_dispo)
                else:
                    context = {'error1': 'Ce Champs doit être de type monnaie FGN.'}
                    return render(request, 'leyssare/leyadmin/user_cotisation.html', context)

            #Ici, on évite que les cases CFA et FGN soient à la fois remplie
            elif montant_cfa != None and montant_fg != None:
                context = {'error':'Les champs CFA et FGN ne peuvent pas être à la fois remplie.'}
                return render(request, 'leyssare/leyadmin/user_cotisation.html', context)

            #On ajoute ici la personne que vient de cotisé à la liste des personnes qui ont cotisé
            usr = VersementLeyssare(nom=nom, prenom=prenom, pays=pays, montant_cfa=montant_cfa, montant_fg=montant_fg)
            usr.save()
            print(nom, prenom, pays)
            context = {'data': 'Utilisateur enregistré avec succés. '}
            return render(request, 'leyssare/leyadmin/user_cotisation.html', context)
        else:
            return render(request, 'leyssare/leyadmin/user_cotisation.html')

#Enregistrer de dépenses
@login_required(login_url='../../../BleyApp/login/')
def montant_depensee(request):

        if request.method == 'POST':
            raison_depense = request.POST.get('raison')
            depense = request.POST.get('montant')
            if (depense and raison_depense) != '' and depense.isdigit():
                #On récupère le montant disponible dans notre caisse
                recup = LeyssareCaisse.objects.all()
                for data_recup in recup:
                    depense = int(depense)
                    #On ajoute le montant qui vient d'être depensé, à la somme totale des dépenses dans notre Caisse
                    data_recup.montant_depencee += depense
                    data_recup.save()
                    print(data_recup.montant_depencee)

                #On ajoute le montant qui vient d'être dépensé dans nos dépenses
                sauvegarder = LeyssareDepenses(nature_de_depense=raison_depense, montant_depensee=depense)
                sauvegarder.save()
                context = {'data':'Montant dépensé'}
                return render(request, 'leyssare/leyadmin/depensee.html', context)
            else:
                context = {'error': 'Tous les champs doivent être remplie '}
                return render(request, 'leyssare/leyadmin/depensee.html', context)
        else:
            return render(request, 'leyssare/leyadmin/depensee.html')


