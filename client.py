import sockets.udp as udp
import sockets.tcp as tcp
import sockets.sctp as sctp

def run(address, protocol, buffer):
    if protocol == 'UDP':
        udp.client(buffer, address)
    elif protocol == 'TCP':
        tcp.client(buffer, address)
    elif protocol == 'SCTP':
        sctp.client(buffer, address)