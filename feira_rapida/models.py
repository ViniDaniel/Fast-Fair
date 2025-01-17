from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vendedor(models.Model):
    UF_CHOICES = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    ]
      
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="vendedor",
        verbose_name="Usuário",
    )

    nome = models.CharField(max_length=200, blank=False, null=False, verbose_name="Nome do Fornecedor")
    cpf = models.IntegerField()
    endereco = models.CharField(max_length=500, blank=False, null=False, verbose_name="Endereço")
    bairro = models.CharField(max_length=50, blank=False, null=False)
    cidade = models.CharField(max_length=50, blank=False, null=False)
    uf = models.CharField(
        max_length=2, choices=UF_CHOICES, verbose_name="UF", blank=False, null=False
    )
    telefone = models.CharField(
        max_length=15, blank=False, null=False, validators=[MinLengthValidator(11)]
    )
    email = models.EmailField(blank=False, null=False)
    outras_informacoes = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="Outras Informações"
    )
    outras_opcoes_de_contato = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="Outras Opções de Contato"
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome_do_produto = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nome do Produto")
    descricao = models.CharField(max_length=500, blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Preço"
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)
    vendedor = models.ForeignKey(
        Vendedor, on_delete=models.CASCADE, related_name="produtos"
    )


class Cliente(models.Model):
    UF_CHOICES = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cliente",
        verbose_name="Usuário",
    )

    nome = models.CharField(max_length=200, blank=False, null=False, verbose_name="Nome do Fornecedor")
    cpf = models.IntegerField()
    endereco = models.CharField(max_length=500, blank=False, null=False, verbose_name="Endereço")
    bairro = models.CharField(max_length=50, blank=False, null=False)
    cidade = models.CharField(max_length=50, blank=False, null=False)
    uf = models.CharField(
        max_length=2, choices=UF_CHOICES, verbose_name="UF", blank=False, null=False
    )
    telefone = models.CharField(
        max_length=15, blank=False, null=False, validators=[MinLengthValidator(11)]
    )
    email = models.EmailField(blank=False, null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome