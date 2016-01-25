def gera_nome_convite(convite):
	posicao_final = len(convite)
	posicao_inicial = posicao_final - 4
	parte1 = convite[0:4]
	parte2 = convite[posicao_inicial: posicao_final]

	# print "%s %s" % (parte1, parte2)
	return parte1 + ' ' + parte2

def envia_convite(nome_convidado):
	print "Enviado Convite para %s" % (nome_convidado)	

def processa_convite(nome_convidadd):
	nome_formatado = gera_nome_convite(nome_convidado)
	envia_convite(nome_formatado)