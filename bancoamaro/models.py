from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.db.models import Sum

# Create your models here.
class ClienteManager(models.Manager):
    def geraUsername(cpf):
        import md5
        m = md5.new(cpf).hexdigest()
        m = m[:10]
        if Cliente.objects.filter(username = m).exists():
        	return geraUsername(m) 
        else :
        	return m

    def createCliente(self, nome, cpf, senha):
    	import md5
    	codigo = md5.new(cpf).hexdigest()
    	codigo = codigo[:10]
    	
    	# codigo = self.geraUsername(cpf)

    	cliente= self.create(nome=nome, cpf=cpf, password=senha, username=codigo)

    	return cliente

    def saldoCliente(self):
        # deposito = Operacao2.objects.filter(tipo_op=1).aggregate(Sum('valor'))
        # saque = Operacao2.objects.filter(tipo_op=2).aggregate(Sum('valor'))
        # return deposito['valor__sum']-saque['valor__sum']
        return 2


    
class Cliente(User):
    # codigo = models.CharField(max_length=10) #username
    nome = models.CharField(max_length=150) 
    cpf=models.CharField(max_length=15)
    # isAdmin=models.IntegerField(default=0) #is_staff
    objects = ClienteManager()
    
# class Operacao(models.Model):
#     id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     valor = models.FloatField()
#     tipo_op = models.IntegerField(default=0)
#     dataHora = models.DateTimeField(auto_now_add = True)

# class Operacao2Manager(models.Manager):
#     def getOpNome(self):
#         return self.operacoes[operacoes.tipo_op]

class Operacao2(models.Model):
    # objects = Operacao2Manager()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.FloatField()
    tipo_op = models.IntegerField(default=0)
    dataHora = models.DateTimeField(auto_now_add = True)
    operacoes={'','Deposito','Saque'}
