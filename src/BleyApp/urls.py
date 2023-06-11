
from django.urls import path, include
from .views import index, accueil, membres, versees, propos, tresorerie, base, liste_membres, membres_ont_versees, \
    depensee, total_depense, capital_restante, gestion_caisse, etat_de_caisse, user_has_cotise, auth_user, \
    membres_registrer, user_versement, montant_depensee, admin_auth, create_account, admin_connexion, admin_deconnexion, \
    admin_index, mention_legal

app_name = 'BleyApp'
urlpatterns = [
    #path('account/', include('django.contrib.auth.urls')),
    path('account/subcribe', create_account, name='usercreation'),

    path('account/adminbase', admin_index, name='AdminIndex'),
    path('login/', admin_connexion, name='AdminAuth'),
    path('account/signup', admin_deconnexion, name='AdminDeAuth'),

    path('account/login/usercreation', membres_registrer, name='usercreation'),
    path('account/login/userversement', user_versement, name='userversement'),
    path('account/login/montantdepensee', montant_depensee, name='montantdepensee'),

    path('', base, name="mybase"),
    path("base/", base, name='mybase'),
    path('index/', index, name='myindex' ),
    path('Authentication/<path:urls>/<str:urls_param>', auth_user, name='authentication'),
    path('accueil/', accueil, name='myaccueil'),
    path('membres/', membres, name='membres'), #Peut être faur revoir les slash à la fin des urls
    path('versees/', versees, name='ontversees'),
    path('versees/ontversees', membres_ont_versees, name='membrescotisee'),
    path('tresorerie/', tresorerie, name='tresorerie'),
    path('tresorerie/depensee', depensee, name='depensee'),
    path('tresorerie/totaldepensee', total_depense, name='totaldepensee'),
    path('tresorerie/capitalrestante', capital_restante, name='capitalrestante'),
    path('a-propos/', propos, name='apropos'),
    path('ListeMembres/', liste_membres, name='ListeMembre'),
    path('tresorerie/etatcaisse', etat_de_caisse, name='etatcaisse'),
    path('Http', gestion_caisse),
    path('user', user_has_cotise),
    path('mention', mention_legal, name='mention_legal'),

    path('sign/', admin_auth, name='AdminPage'),


]

