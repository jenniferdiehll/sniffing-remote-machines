import socket
import sniffer

def client(buffer, address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    data = sock.recv(buffer).decode('UTF-8')
    print(f'Dados recebidos do {address}\n{data}')
    sock.close()


def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen()

    while True:
        # Aguarda uma conexão
        print ('Aguardando uma conexão...')
        connection, client_address = sock.accept()
        # Mostra quem conectou
        print ('Cliente conectado: ', client_address)
        packets = sniffer.runTcpDump()
        connection.send(str.encode(str(packets)))