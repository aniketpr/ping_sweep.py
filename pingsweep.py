# https://manpages.debian.org/testing/fping/fping.8.en.html
# https://docs.python.org/3.6/library/subprocess.html#subprocess.run
# https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap
import subprocess
import sys
import nmap

ip_addres = sys.argv[1]

targets = []

p1 = subprocess.run(['fping','-g','--alive','--quiet',ip_addres], capture_output=True, text=True)

for i in p1.stdout.split('\n'):
	targets.append(i)
		
print(targets)
ports = '21-443'

nmScan = nmap.PortScanner()

#for i in targets:
	#nmScan.scan(i, ports)
	#nmScan[i].has_tcp(443)
	#do somthing......
		
	
