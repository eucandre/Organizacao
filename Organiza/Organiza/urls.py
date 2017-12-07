#Cria as rotas do sistema

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
