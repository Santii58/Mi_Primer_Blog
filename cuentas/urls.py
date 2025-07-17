from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(
         template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
         template_name='registration/password_change.html'),
         name='password_change'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_complete.html'),
        name='password_change_done'),

    path('perfil/', views.PerfilDetalle.as_view(), name='perfil'),
    path('perfil/editar/', views.PerfilEditar.as_view(), name='editar_perfil'),
]
