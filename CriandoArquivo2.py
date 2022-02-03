# Cria arquivo mesmo que ja exista outro com o mesmo nome. 10 tentativas extras.

try:		
	objeto_arquivo = open("Nome_do_arquivo.txt", "x")	
	
except FileExistsError:
	for x in range(10):
		try:
			objeto_arquivo = open(f"Nome_do_arquivo({x}).txt", "x")
			break
		except FileExistsError:
			pass


objeto_arquivo.write("Cria arquivo mesmo que ja exista outro com o mesmo nome. 10 tentativas extras.")
print('Arquivo criado com sucesso.')

objeto_arquivo.close()

try:
	objeto_arquivo = open(f"Nome_do_arquivo{x}.txt", "r")
except:
	objeto_arquivo = open("Nome_do_arquivo.txt", "r")
print(objeto_arquivo.read())
objeto_arquivo.close()
