from django import forms
from .models import Vendedor, Produto, Cliente
import re

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = "__all__"
        labels = {
            "nome": "Nome do Vendedor",
            "cpf": "CPF",
            "endereco": "Endereço",
            "bairro": "Bairro",
            "cidade": "Cidade",
            "uf": "UF",
            "telefone": "Telefone",
            "email": "E-mail",
            "outras_informacoes": "Outras Informações",
            "outras_opcoes_de_contato": "Outras Opções de Contato",
        }
        def clean_cpf(self):
            cpf = self.cleaned_data.get("cnpj")
            if not re.match(r"^\d{11}$", cpf):
                raise forms.ValidationError("O CPF deve conter exatamente 11 dígitos.")
            return cpf

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
        labels = {
            "nome_do_produto": "Nome do Produto",
            "descricao": "Descrição",
            "preco": "Preço",
            "fornecedor": "Fornecedor",
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        labels = {
            "nome": "Nome do Cliente",
            "cpf": "CPF",
            "endereco": "Endereço",
            "bairro": "Bairro",
            "cidade": "Cidade",
            "uf": "UF",
            "telefone": "Telefone",
            "email": "E-mail",
        }
        def clean_cpf(self):
            cpf = self.cleaned_data.get("cnpj")
            if not re.match(r"^\d{11}$", cpf):
                raise forms.ValidationError("O CPF deve conter exatamente 11 dígitos.")
            return cpf