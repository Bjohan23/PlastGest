from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('lista_productos')),  # Redirige desde / a /productos/
    path('', include('inventario.urls')),  # Solo esta vez
    
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='inventario/password_reset_form.html'),
         name='password_reset'),

    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='inventario/password_reset_done.html'), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='inventario/password_reset_confirm.html'), 
         name='password_reset_confirm'),

    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='inventario/password_reset_complete.html'), 
         name='password_reset_complete'),
]
