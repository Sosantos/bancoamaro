from django.conf.urls import url
from.import views
# from django.contrib.auth.decorators import permission_required

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nova-conta$', views.novaConta, name='novaConta'),
    url(r'^cadastra-nova-conta$', views.novoUsuario, name='novoUsuario'),
    url(r'^entrar$', views.logar, name='logar'),
    url(r'^sair$', views.sair, name='sair'),
    url(r'^correntista$', views.correntista, name='correntista'),
    url(r'^operacao$', views.operacao, name='operacao'),
    url(r'^administracao$', views.administracao, name='administracao'),
    url(r'^relatorio-cliente/(?P<cliente_id>[0-9]+)/$', views.relatorioCliente, name='relatorioCliente'),
]


