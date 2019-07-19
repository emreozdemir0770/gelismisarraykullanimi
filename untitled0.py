import subprocess
import ipaddress
from subprocess import Popen, PIPE
network = ipaddress.ip_network("192.168.100.103")
for i in network.host():
    i=str(i)
    toping = Popen(['ping','-c','3',i], stdout=PIPE)
    output=toping.communicate()[0]
    hostalive=toping.returncode
    if hostalive ==0:
        print(i,'is reachable')
    else:
        print(i,'is unreachable')