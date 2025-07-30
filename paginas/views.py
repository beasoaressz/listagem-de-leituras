from django.views.generic import TemplateView
# from django.shortcuts import render

# Create your views here.

# def meus_livros(request):
#     livros_lendo = ["Dom Casmurro", "1984", "O Pequeno Príncipe"]
#     return render(request, "paginas/index.html", {"livros_lendo": livros_lendo})

class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livros_lendo'] = ["Dom Casmurro", "1984"]
        context['livros_quero_ler'] = ["A Revolução dos Bichos", "O Hobbit"]
        context['livros_concluidos'] = ["Capitães da Areia", "Orgulho e Preconceito"]
        return context

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'