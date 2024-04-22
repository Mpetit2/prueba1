vlan_normal=range(1,1005)
vlan_extendida=range(1006,4094)
numero_vlan= int(input("ingresa numero de vlan:"))
if numero_vlan in vlan_normal:
    print ("el numero de vlan:",numero_vlan,"es normal")
elif numero_vlan in vlan_extendida:
    print("el numero de vlan:",numero_vlan,"es extendida")
else:
    print("el numero de vlan:",numero_vlan,"no corresponde")
