import sockets.sctp as sctp
import sockets.tcp as tcp
import sockets.udp as udp

def run(address, protocol):
    buffer = 2048
    if protocol == 'UDP':
        udp.server(buffer, address)
    elif protocol == 'TCP':
        tcp.server(address)
    elif protocol == 'SCTP':
        sctp.server(address)