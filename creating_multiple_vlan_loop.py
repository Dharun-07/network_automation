import telnetlib
import getpass
print('''============================================================================
                          TELNET
============================================================================                        
                    NETWORK AUTOMATION
============================================================================''')   
host="192.168.0.1"
name=input("Enter your Username")
tn=telnetlib.Telnet(host)
passw=getpass.getpass()
tn.read_until(b"Username:")
tn.write(b"name"+b"\n")
if(passw):
    tn.read_until(b"password:")
    tn.write(b"passw"+b"\n")
tn.write(b"enable\n")
tn.write(b"conf t\n")
for i in range(2,10):
    tn.write(b"vlan"+str(i).encode('ascii')+b"\n")
    tn.write(b"name vlan_"+str(i).encode('ascii')+b"\n")
    tn.write(b"no shut \n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))