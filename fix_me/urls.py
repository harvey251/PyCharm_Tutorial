from django.urls import path

from fix_me.views.index import index

urlpatterns = [
    path('', index, name='index'),
]