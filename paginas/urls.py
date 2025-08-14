from django.urls import path
from .views import PaginaInicial, PerfilView

# define a url padrao para a pagina inicial
urlpatterns = [
    # path:('endereco', MinhaView.asview(), name='nome_da_url')
    path('', PaginaInicial.as_view(), name='inicio'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
]