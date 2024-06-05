import socket

server_address = (('localhost', 8000))
client_socket = socket.socket ()

print ('Intentando conectar con el servidor en {server_address}')
client_socket.connect(server_address)

mensaje_inicial = "Hola, servidor!/n".encode('utf-8')
client_socket.sendall(mensaje_inicial)

mensaje_bienvenida = client_socket.recv(1024)
print('mensaje del servidor:{mensaje_bienvenida.decode("utf-8")}')

while True:

	mensaje_cliente = input ('ingresa un mensaje al servidor:')
	mensaje_cliente = mensaje_cliente + '/n'
	client_socket.sendall(mensaje_cliente.encode('utf-8'))

	respuesta_servidor = client_socket.recv(1024)
	print('Respuesta del servidor: {respuesta_servidor.decode("utf-8")}')
    
client_socket.close()
print ("conexion con el servidor finalizada. ")

client_socket.close()
