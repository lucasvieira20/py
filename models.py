# -*- coding: UTF-8 -*-
class Perfil(object):
	# Função Construtora __init__ 
	# Função Construtura sempre com __ no inicio e final
	
	def __init__(self,nome,telefone,empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa

	def imprimir(self):
		print "Nome : %s, Telefone: %s, Empresa %s" % (self.nome,self.telefone, self.empresa)


class Data(object):
	def __init__(self,dia,mes,ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

		def imprime(self):
			print '%s/%s/%s' % (self.dia, self.mes, self.ano)