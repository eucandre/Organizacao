import django_filters
from django.contrib.auth.models import User
from .models import User

class ColaboradorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username', 'telphone', 'office', ]