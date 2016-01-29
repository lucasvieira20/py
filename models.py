# -*- coding: UTF-8 -*-
class Perfil(object):
	# Função Construtora __init__ 
	# Função Construtura sempre com __ no inicio e final
	'Classe de Usuários'
	def __init__(self,nome,telefone,empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print "Nome : %s, Telefone: %s, Empresa %s" % (self.nome,self.telefone, self.empresa)

	def curtir(self):
		self.__curtidas+=1

	def obter_curtidas(self):
		return self.__curtidas

class Perfil_Vip(Perfil):
	# Função Construtora __init__ 
	# Função Construtura sempre com __ no inicio e final
	
	'Classe de Usuários Vips'

	def __init__(self,nome,telefone,empresa,apelido):
		# Herdando dados da classe Pai
		super(Perfil_Vip, self).__init__(nome,telefone,empresa)
		self.apelido = apelido

	def obter_creditos(self):
		#Primeiro Paramentro nome da classe filha
		#Super usada para acessar a classe pai através da filha
		return super(Perfil_Vip,self).obter_curtidas() * 10.0


class Data(object):
	def __init__(self,dia,mes,ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

		def imprime(self):
			print '%s/%s/%s' % (self.dia, self.mes, self.ano)

class Pessoa(object):
	def __init__(self,nome,peso,altura):
		self.nome = nome
		self.peso = peso
		self.altura = altura

	def imprime_imc(self):
		imc = self.peso/ (self.altura)
		print "Imc de %s: %s" % (self.nome, imc)


class Retangulo(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.__area = x * y

	def obter_area(self):
		return self.__area