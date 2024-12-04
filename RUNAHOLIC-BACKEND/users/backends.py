# users/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        # Tenta encontrar o usuário pelo email primeiro
        user = User.objects.filter(email=username).first() or User.objects.filter(username=username).first()

        # Verifica se encontrou o usuário e se a senha está correta
        if user and user.check_password(password):
            return user
        return None
