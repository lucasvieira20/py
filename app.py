# -*- coding: UTF-8 -*-
def cadastrar(nomes):
    print 'Digite: o nome:'
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
	print "Qual nome gostaria de remover ?"
	nomes = raw_input()
	nomes.remove(nome)

def alterar(nomes):
	print "Qual nome você gostaria de alterar"
	nome_a_remover = raw_input()

	if(nome_a_remover in nomes):
		posicao = nomes.index(nome_a_remover)
		print "Digite o novo nome :"
		nome_novo = raw_input()
		nomes[posicao] = nome_novo

def procurar(nomes):
	print "Digite o nome a procurar"
	nome = raw_input()
	if(nome in nomes):
		print "Nome %s está cadastrado " % (nome)
	else:
		print "Nome %s não está cadastrado" % (none)


def procurar_regex(nomes):
	print("Digite a Expressão Regular")
	regex = raw_input()
	nomes_concatenados = " " .join(nomes)
	resultados = re.findall(regex, nomes_concatenados)
	print(resultados)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):    
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar , 6 para regex'
        escolha = raw_input()
        if(escolha == '1'):
            cadastrar(nomes)
        if(escolha == '2'):
            listar(nomes)    
        if(escolha == '3'):
        	remover(nomes)
        if(escolha == '4'):
        	alterar(nomes)
        if(escolha == '5'):
        	procurar(nomes)
        if(escolha == '6'):
        	procurar_regex(nomes)
def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome
menu()