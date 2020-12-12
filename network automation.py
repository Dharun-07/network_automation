import telnetlib
import getpass
host="192.168.43.1"
tn=telnetlib.Telnet(host)
name=input(str("Enter the username to connect to telnet:"))
passw=getpass.getpass()
tn.read_until("Username:")
tn.write(name.encode()+b"\n")
if passw:
    tn.read_until("Password")
    tn.write(passw.encode()+b"\n")

tn.write(b"enable\n")
tn.write(b"conf t\n")
tn.write(b"int vlan 10\n")
tn.write(b"ip addr 192.168.1.1 255.255.255.0\n")
tn.write(b"no shut\n"))
tn.write(b"exit()\n")
