# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.template.context import RequestContext

from bancoamaro.models import Cliente, Operacao2

# Create your views here.

########## Visitante

def index(request):
	if not request.user.is_authenticated():
		return render(request,'inicial/index.html')
	if request.user.is_staff:
		return render(request,'administracao/index.html')
	return render(request,'correntista/index.html')

def novaConta(request):

	return render(request,'inicial/novaConta.html')

def novoUsuario(request):
	if request.method == "POST":
		if Cliente.objects.filter(cpf = request.POST.get('cpf')).exists():
			return render(request, 'inicial/novaConta.html', {
				'error_message': "CPF já cadastrado.",
			})
		else:
			Cliente.objects.createCliente(nome = request.POST.get('nome'),cpf = request.POST.get('cpf'),senha = request.POST.get('senha'))
			return render(request,'inicial/novoUsuario.html')
	else:
		return render(request,'inicial/novaConta.html')

def logar(request):
	if request.user.is_staff:
		return render(request,'administracao/index.html')

	if request.method == "POST":
		codigo = request.POST.get('codigo')
		senha = request.POST.get('senha')
		user = authenticate(username=codigo, password=senha)

		if user is not None:
			if user.is_staff:
				return render(request,'administracao/index.html')
			return render(request,'correntista/index.html')
		else:
			return render(request,'inicial/login.html', {
				'error_message': "Codigo ou senha inválidos",
			})
	else:
		return render(request,'inicial/login.html')

def sair(request):
	logout(request)
	return render(request,'inicial/login.html')

########## Correntista
@login_required(login_url='bancoamaro:logar')
def correntista(request):
	# cl = Cliente.objects.filter(username = request.user.username)
	# saldo = cl.objects.saldoCliente()
	saldo = Cliente.objects.saldoCliente()

	if request.method == "POST":
		return render(request,'correntista/index.html')

	return render(request,'correntista/index.html', {
		'saldo': saldo,
	})

def operacao(request):
	if request.method == "POST":

		tipo_op = request.POST.get('tipo_op')
		valor = request.POST.get('valor')
		id_cliente = Cliente.objects.order_by('?').first()
		# id_cliente = Cliente.objects.filter(pk=request.user.id).first()


		o = Operacao2.objects.create(tipo_op=tipo_op, valor=valor, id_cliente=id_cliente)
		o.save()

		return render(request,'correntista/index.html',{
				'message':"Operação realizada com sucesso"
			})
	else:
		return render(request,'correntista/index.html')


########## Admin
def administracao(request):
	clientes = Cliente.objects.filter(is_staff=False)

	return render(request,'administracao/index.html', {
		'clientes': clientes
	})

def relatorioCliente(request, cliente_id):

	cliente = Cliente.objects.filter(pk=cliente_id)
	if cliente.exists():
		cliente = cliente[0]
		operacoes = Operacao2.objects.filter( id_cliente=cliente_id).order_by('-dataHora')
		# cliente = operacoes[0].id_cliente

		return render(request,'administracao/relatorioCliente.html', {
			'operacoes': operacoes,
			'cliente': cliente
		})
	else:
		return render(request,'administracao/index.html', {
			'error_message': 'Cliente não existe'
		})

# def ajax_porDia(request):
# 	if request.is_ajax():
		# data = request.GET.get('dateText')

		# deposito = Operacao2.objects.filter(tipo_op=1, dataHora=datetime(2008, 03, 27)).aggregate(Sum('valor'))
  #       saque = Operacao2.objects.filter(tipo_op=2, dataHora=datetime(2008, 03, 27)).aggregate(Sum('valor'))
  #       deposito=deposito['valor__sum']
  #       saque=['valor__sum']

	    # return render_to_response( 'results.html', { 'deposito': 3,'saque': 4, }, 
	    #                            context_instance = RequestContext( request ) )
