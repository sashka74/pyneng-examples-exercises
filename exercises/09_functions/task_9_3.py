# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

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
    return access_dict,trunk_dict

print(get_int_vlan_map('config_sw1.txt'))