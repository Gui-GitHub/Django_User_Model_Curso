from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUsuario


# Formulário para criação de usuário customizado
class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
        labels = {'username': 'Username/E-mail'}

    # Salva o usuário com senha e e-mail definidos corretamente
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


# Formulário para alteração de usuário customizado
class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')

