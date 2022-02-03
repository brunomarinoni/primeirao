# linhas de comando para criar arquivo




# para criar o arquivo se utiliza uma funcao que retorna uma referencia para um objeto
objeto_arquivo = open("Nome_do_arquivo.txt", "x") 
		
		
objeto_arquivo.write("O que voce escreve aqui vai ser o conteudo do arquivo. Repare que estamos criando um arquivo com a extensao txt, mas voce pode criar arquivos em outros formatos. \nImportante lembrar que se nao for um arquivo de texto (considerado o padrao) eh preciso utilizar a letra 'b' no segundo parametro quando a funcao que modifica o arquivo eh chamada.")
print('Arquivo criado com sucesso.\n\n')

objeto_arquivo.close()





# reabrindo o arquivo para leitura utilizamos a mesma funcao mas com outro parametro
# fechamos o arquivo e reabrimos para que a leitura retorne ao inicio do conteudo do arquivo 

objeto_arquivo = open("Nome_do_arquivo.txt", "r")
 
print(objeto_arquivo.read())

objeto_arquivo.close()

