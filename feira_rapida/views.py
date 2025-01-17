from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Vendedor, Produto, Cliente
from .forms import VendedorForm, ProdutoForm, ClienteForm  # Importe os formulários do forms.py

# Create your views here.
def home(request):
    return render(request, "feira_rapida/home.html")


class VendedorListView(ListView):
    model = Vendedor
    #template_name = "todos/fornecedor_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(nome__icontains=query)
                | Q(cpf__icontains=query)
                | Q(endereco__icontains=query)
                | Q(cidade__icontains=query)
                | Q(telefone__icontains=query)
            )
        return queryset


class VendedorCreateView(CreateView):
    model = Vendedor
    form_class = VendedorForm  
    template_name = "feira_rapida/vendedor_form.html"
    success_url = reverse_lazy("home")
    extra_context = {"titulo": "Cadastrar Vendedor"}


class VendedorUpdateView(UpdateView):
    model = Vendedor
    form_class = VendedorForm  # Use o formulário personalizado
    success_url = reverse_lazy("home")
    extra_context = {"titulo": "Atualizar Vendedor"}


class VendedorDeleteView(DeleteView):
    model = Vendedor
    template_name = "feira_rapida/vendedor_confirm_delete.html"
    success_url = reverse_lazy("home")


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm  # Use o formulário personalizado
    template_name = "feira_rapida/produtos_form.html"
    success_url = reverse_lazy("home")
    extra_context = {"titulo": "Cadastrar Produto"}


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm  # Use o formulário personalizado
    template_name = "feira_rapida/produtos_form.html"
    success_url = reverse_lazy("home")
    extra_context = {"titulo": "Atualizar Produto"}


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = "feira_rapida/produtos_confirm_delete.html"
    success_url = reverse_lazy("home")


class ProdutosPorFornecedorListView(ListView):
    model = Produto
    template_name = "feira_rapida/produtos_por_vendedor.html"
    context_object_name = "produtos"

    def get_queryset(self):
        vendedor_id = self.kwargs["vendedor_id"] 
        return Produto.objects.filter(vendedor__id=vendedor_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inclua o vendedor no contexto para mostrar seus detalhes na página
        context["vendedor"] = get_object_or_404(
            Vendedor, id=self.kwargs["vendedor_id"]
        )
        return context

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm  
    template_name = "feira_rapida/cliente_form.html"
    success_url = reverse_lazy("home")
    extra_context = {"titulo": "Cadastrar Cliente"}


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm  # Use o formulário personalizado
    success_url = reverse_lazy("home")
    extra_context = {"titulo": "Atualizar Cliente"}


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "feira_rapida/cliente_confirm_delete.html"
    success_url = reverse_lazy("home")