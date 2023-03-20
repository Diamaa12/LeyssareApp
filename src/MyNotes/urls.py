from django.urls import path, include

from .views import mamadou_notes, samed_notes, user_login, logout_view, mamadou_items_del, samed_items_del
app_name = 'Mynotes'
urlpatterns = [
    #path('Import/', export_data, name='exportation'),
    #path('account/', include('django.contrib.auth.urls')),
    path('login/', user_login, name='login-user'),
    path('logout/', logout_view, name='logout-user'),
    path('mamadou/', mamadou_notes, name="mamadou-notice"),
    path('mamadou/<int:id>', mamadou_items_del, name="mamadou_items_del"),
    path('samed/', samed_notes, name='samed-notice'),
    path('samed/<int:id>', samed_items_del, name="samed_items_del"),
    ]