from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Produto
import re







class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search("[a-zA-Z]+-[a-zA-Z]+",username): #
            raise forms.ValidationError("O formato do Usuário deve ser 'área-usuário'") 
        return username

class ProdutoModel2Form(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','qtd','setor']
        
        