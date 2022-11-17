import sctp
import sniffer
import socket

def client(buffer, address):
    sock = sctp.sctpsocket_tcp(socket.AF_INET)
    sock.connect(address)
    data = sock.recv(buffer).decode('UTF-8')
    print(f'Dados recebidos do {address}\n{data}')
    sock.close()


def server(address):
    sock = sctp.sctpsocket_tcp(socket.AF_INET)
    sock.bind(address)
    sock.listen(1)

    while True:
        print ('Aguardando uma conexão...')
        connection, client_address = sock.accept()
        print ('Cliente conectado: ', client_address)
        packets = sniffer.runTcpDump()
        connection.send(str.encode(str(packets)))