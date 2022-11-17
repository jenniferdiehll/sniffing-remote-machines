import os

def runTcpDump():
    return os.popen('tcpdump -i eth0 -c 10 -v').read()