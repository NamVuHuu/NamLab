import netmiko
from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "ip": "10.18.8.150",
    "username": "vnpro",
    "password": "vnpro#123",
    "secret": "vnpro#321"
}
ConnectHandler(**router)

ConnectHandler(**router).send_command("show ip interface brief")
print(ConnectHandler(**router).send_command("show ip interface brief"))

connect = ConnectHandler(**router)
connect.enable()

print(connect.send_command("show run"))

print(connect.send_config_set("hostname R1-Nam"))

for i in range(1, 4):
        print(connect.send_config_set(["int e0/"+ str(i),"ip add 1.2."+str(i)+".1 255.255.255.0", "no shut"]))

interface = {
        "e0/1":"192.168.1.1",
        "e0/2":"192.168.1.2"
} 
print(connect.send_command("show ip int br"))

connect.disconnect