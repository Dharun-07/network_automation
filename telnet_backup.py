import telnetlib
import getpass
print('''============================================================================
                          TELNET
============================================================================                        
                    NETWORK AUTOMATION
============================================================================''')
name=input("Enter Telnet username:")
passw=getpass.getpass()
f=open("myswitch",r)
for i in f:
    host=i.strip()
    tn=telnetlib.Telnet(host)
    tn.read_until("Username:")
    tn.write(name.encode()+b"\n")
    if passw:
        tn.read_until("Password")
        tn.write(passw.encode()+b"\n")
    tn.write(b"terminal length 0 \n")
    tn.write(b"sh run \n")

    read=tn.read_all()
    save=open("switch_"+host,"w")
    save.write(read.decode('ascii'))
    save.write("\n")
f.close()


