from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('create_account/', views.create_account, name='create_account'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('set_password/<uidb64>/<token>', views.set_password, name='set_password')
]
