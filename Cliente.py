import socket

HOST = '127.0.0.1'      # Endereco IP Servidor (localhost)
PORT = 50000            # Porta Servidor (aleatoria, mas se deve escolher numeros altos para evitar conflito com outros processos padroes

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	 #define ipv4 e TCP
tcp.connect((HOST, PORT))  #do lado do servidor seria tcp.bind

print('Enviando mensagem para o servidor..')
tcp.sendall(str.encode('Bom dia!'))

print('Resposta do servidor:')
data = tcp.recv(1024)
print(data.decode())
