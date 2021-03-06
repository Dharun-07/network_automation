from netmiko import ConnectHandler

ios1_l2={
    'device_type':'cisco_ios',
    'ip':'192.168.0.2',
    'username':'cisco',
    'password':'cisco',
}

ios2_l2={
    'device_type':'cisco_ios',
    'ip':'192.168.0.3',
    'username':'cisco',
    'password':'cisco',
}

ios3_l2={
    'device_type':'cisco_ios',
    'ip':'192.168.0.3',
    'username':'cisco',
    'password':'cisco',
}

devices=[ios1_l2,ios2_l2,ios3_l2]
for i in devices:
    connect=ConnectHandler(**i)
    output=connect.send_command("sh int br")
    print(output)
    for j in range(2,10):
        print("creating vlan_"+str(j))
        command=["vlan"+str(j),"name vlan_"+str(j)]
        output=connect.send_conf_set(command)
        print(output)