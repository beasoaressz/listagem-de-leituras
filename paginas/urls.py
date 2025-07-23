from django.urls import path
from .views import HomePageView

# define a url padrao para a pagina inicial
urlpatterns = [
    # path:('endereco', MinhaView.asview(), name='nome_da_url')
    path('', HomePageView.as_view(), name='inicio'),
]