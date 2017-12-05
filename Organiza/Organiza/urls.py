#Cria as rotas do sistema

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app_org.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Apresentacao),
    url(r'^Organizacao', Cria_Organizacao),
    url(r'^Unidade_comercial/', Cria_Unidade_Comercial),
    url(r'^Marca/', Cria_Marca),
    url(r'^Regional/', Cria_Regional),
    url(r'^Colaborador/', Cria_Colaborador),
    url(r'^Linha_Produto/', Cria_Linha_Produto),
    url(r'^Produto/', Cria_Produto),
    url(r'^cliente/', Cria_Cliente),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
