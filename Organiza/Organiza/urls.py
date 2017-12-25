#Cria as rotas do sistema

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app_base.views import *
from app_usuario.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', apresentacao),
    url(r'^CriaUsuario',Cria_usuario),
    url(r'^lista_usuarios',lista_usuarios),
    url(r'^item_usuario/(?P<nr_item>\d+)/$', detalha_usuario),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
