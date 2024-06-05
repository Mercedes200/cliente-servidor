import socket

server_socket = socket.socket ()
server_address =(('localhost', 8000 ))
server_socket.bind(server_address)
server_socket.listen (5)

print ('servidor en espera de conexiones.....')
client_socket, client_address = server_socket.accept ()

print ('conectado con {client_address}')
mensaje_bienvenida = "Bienvenido al servidor!/n".encode('utf-8')
client_socket.sendall(mensaje_bienvenida)

while True:
   datos_recibido = client_socket.recv(1024)
   if not  datos_recibido:
    break

    datos_decoficados = datos_recibido.decode('utf-8')
    print ("recibido del cliente: {datos_decoficados}")

    respuesta = "su mensaje fue: {datos_decoficados}".encode('utf-8')
    client_socket.sendall(respuesta)


client_socket.close ()
