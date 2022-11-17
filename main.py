import client
import json
import server
import socket
import threading
import time

if __name__ == "__main__":

    protocol = ''

    while True:
        protocol = input('Informe o protocolo: [UDP, TCP, SCTP] ')
        if protocol in ('UDP','TCP','SCTP'):
            break

    with open("address.json", encoding='utf-8') as address:
        addresses = json.load(address)

    clientAddresses = []
    serverAddress = ("",0)
    host = socket.gethostname()
    IPAddr = socket.gethostbyname(host)
    buffer = 2048
        
    for i in range(len(addresses)):
        
        if addresses[i]['host'] == IPAddr:
            serverAddress = (addresses[i]['host'], addresses[i]['port'])
        else:
            clientAddresses.append((addresses[i]['host'], addresses[i]['port']))

    serverThread = threading.Thread(target=server.run, args=(serverAddress, protocol))
    serverThread.start()
    time.sleep(5)


    for i in range(len(clientAddresses)):
        client.run(clientAddresses[i], protocol, buffer)