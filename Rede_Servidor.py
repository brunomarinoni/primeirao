import socket


HOST = 'localhost'        # Endereco IP Servidor local (considerando que o uso vai ser domestico)
PORT = 50000            	# Porta Servidor (aleatoria, mas se deve escolher numeros altos para evitar conflito com outros processos padroes


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#define ipv4 e TCP
tcp.bind((HOST, PORT))		#do lado do cliente seria tcp.connect


tcp.listen()		
print('Aguardando a conexao de um cliente..')
conexao, cliente = tcp.accept()		#estabelece a conexao e retorna o endereco da conexao
print ('Concetado com ', cliente)


while True:
	msg = conexao.recv(1024)		#recebe e limita o conteudo dos dados transmitidos
	if not msg: 
		print('Conexao encerrada com ', cliente)
		conexao.close()
		break
	conexao.sendall(msg)
	print ("Dados de ", cliente, "recebidos: ", msg.decode())
