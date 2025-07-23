from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    # ao digitar a URL raiz, o Django irá renderizar o template index.html
    template_name = 'paginas/index.html'
