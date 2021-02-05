from netmiko import ConnectHandler

ios_l2={
    'device_type':'cisco_ios',
    'ip':'192.168.0.3',
    'username':'cisco',
    'password':'cisco',
}

connect=ConnectHandler(**ios_l2)
output=connect.send_command("sh ip int br")
print(output)

config_commands=["int loop 0","ip address 1.1.1.1 255.255.255.0"]
output=connect.send_conf_set(config_commands)
print(output)

for i in range(2,10):
    print("creating vlan_"+str(i))
    config_commands=["vlan"+str(i),"name vlan_"+str(i)]
    output=connect.send_conf_set(config_commands)
    print(output)
    