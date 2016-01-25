# -*- coding: UTF-8 -*-
class Perfil(object):
	# Função Construtora __init__ 
	# Função Construtura sempre com __ no inicio e final
	
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