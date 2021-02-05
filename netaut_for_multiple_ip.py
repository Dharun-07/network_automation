import telnetlib
import getpass
print('''============================================================================
                          TELNET
============================================================================                        
                    NETWORK AUTOMATION
============================================================================''')

name=input("Enter the Telnet Username:")
passw=getpass.getpass()
f=open("myswitch","r")
for i in f:
    host=i.strip()
    tn=telnetlib.Telnet(host)
    tn.read_until("Username:")
    tn.write(name.encode('ascii')+b"\n")
    if(passw):
        tn.read_until("password:")
        tn.write(passw.encode('ascii')+b"\n")
        for i in range(2,10):
            tn.write(b"vlan"+str(i).encode('ascii')+b"\n")
            tn.write(b"name vlan_"+str(i).encode('ascii')+b"\n")
            tn.write(b"no shut\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    f.close()
