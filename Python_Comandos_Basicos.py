# Este arquivo foi criado como exercicio de fixacao com o objetivo de decorar e compartilhar o mais basico da linguagem python. Se voce executa-lo ele vai funcionar como um programa basico.
# Toda linha iniciada com o simbolo "#" funciona apenas como comentario e nao tem nenhum efeito no codigo.



# output
print('Este eh um programa de demonstracao de acoes basicas do Python. \n')		#\n serve para quebrar o paragrafo
print('Com a funcao "print()" voce define uma saida de texto no terminal.')			

# input
resposta = input('Com a funcao "input()" voce define uma entrada de texto atraves do terminal. \nEscreva algo e confira.')
print('')

# formatar string
print ('Voce pode pre-definir um trecho do texto que sera modificado a partir de uma entrada do usuario. \nBasta utilizar "f" seguido do texto e inserindo {} na lacuna em que se deve posicionar a insercao.')
print (f"Voce escreveu anteriormente '{resposta}' e nos incluimos a sua resposta na nossa saida.\n")



# teste de condicoes
if resposta == 'eu sei':
	print('Voce ja nao eh mais um iniciante.')
else:
	print('Agora voce ja pode utilizar esse recurso.\n')



# variaveis

var1 = 'Uma variavel pode ser de varios tipos. Esta eh uma variavel do tipo "string" e ao ser atribuida precisa estar entre aspas simples ou duplas. \nAbaixo voce tem uma variavel do tipo "integer".'
var2 =  9
print(var1)
print(var2, '\n')



# definir funcao
def funcao():
	print('Esta funcao ensina a criar e a fazer uma funcao funcionar.\n')
funcao()



# definir uma classe com um metodo construir um objeto
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  def cumprimento(self): 						#metodo eh o nome da funcao que pertence aa classe
    print("Oi! Muito prazer, " + self.nome + ". Abra o codigo e veja como foi facil construir esse programa basico.")


p1 = Pessoa(input("Qual seu nome?"), input("Quantos anos voce tem?"))
print(p1.nome)
print(p1.idade)
print('') 
p1.cumprimento()

