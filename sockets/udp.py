import socket
import sniffer

def client(buffer, address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes('Want Packet' ,'UTF-8'), address)
    bytesAddressPair = sock.recvfrom(buffer)
    data = bytesAddressPair[0].decode("UTF-8") 
    print(data)

def server(buffer, address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(address)

    while True:
        bytesAddressPair = sock.recvfrom(buffer)
        client_address = bytesAddressPair[1]
        packets = sniffer.runTcpDump()
        sock.sendto(bytes(packets ,'UTF-8'), client_address)