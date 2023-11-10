from django.shortcuts import render
from .models import CustomUser
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from .models import CustomUser
from django.http import Http404
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm


User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirecionar para a página de perfil após o login
            return redirect('profile')  # Substitua 'profile' pelo nome da sua view de perfil
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'
            return render(request, 'users/login.html', {'error_message': error_message})
    else:
        # Se não for um POST, apenas renderize a página de login
        return render(request, 'users/login.html')

def password_reset(request):
    # Logic for user registration page
    return render(request, 'users/password_reset.html')

def create_account(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        squad = request.POST.get('squad')
        function = request.POST.get('function')

        # Validar o e-mail para garantir que seja único
        if CustomUser.objects.filter(email=email).exists():
            error_message = 'E-mail já cadastrado.'
            return render(request, 'users/create_account.html', {'error_message': error_message})

        # Criar o usuário com o status inativo
        user = CustomUser.objects.create_user(name, email, squad, function, is_active=False)
        user.set_unusable_password()
        user.save()

        # Enviar e-mail para o usuário ativar sua conta
        send_activation_email(user)

        return redirect('login')  # Redirecionar para a página de login
    else:
        return render(request, 'users/create_account.html')


def send_activation_email(user):
    current_site = get_current_site(None)
    mail_subject = 'Ative sua conta no SGTestes'
    message = render_to_string('users/activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })

    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(CustomUser, pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')  # Redirecionar para a página de login após ativar a conta
    else:
        return render(request, 'users/activation_invalid.html')


def set_password(request, uidb64, token):
    """View para definir uma nova senha para um usuário."""

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(CustomUser, pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        return render(request, 'users/activation_invalid.html')

    if not default_token_generator.check_token(user, token):
        return render(request, 'users/activation_invalid.html')

    form = SetPasswordForm(user=user, data=request.POST or None)

    if form.is_valid():
        form.save()
        user = authenticate(username=user.username, password=form.cleaned_data['new_password1'])
        login(request, user)
        return redirect('home')

    return render(request, 'users/set_password.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validar o e-mail e a senha
        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            # Redirecionar para a página de perfil após o login
            return redirect('profile')  # Substitua 'profile' pelo nome da sua view de perfil
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'
            return render(request, 'users/login.html', {'error_message': error_message})
    else:
        # Se não for um POST, apenas renderize a página de login
        return render(request, 'users/login.html')
