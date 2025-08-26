# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    access_dict={}
    trunk_dict={}
    with open(config_filename, 'r') as f:
        for line in f:
            if 'interface' in line:
                iface = line.split()[1]
            elif 'switchport trunk allowed' in line and iface:
                vlans = line.split()[-1].split(',')
                trunk_dict[iface] = [int(vlan) for vlan in vlans]
            elif 'switchport access vlan' in line and iface:
                ac_vlans = int(line.split()[-1])
                access_dict[iface] = ac_vlans
            elif 'switchport mode access' in line and iface:
                access_dict[iface] = 1
    return access_dict,trunk_dict

print(get_int_vlan_map('config_sw2.txt'))