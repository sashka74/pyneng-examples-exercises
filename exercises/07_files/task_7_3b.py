# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vl = input(f"Введите номер VLAN: ")

entries = []

with open('CAM_table.txt') as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[0].isdigit():
            vlan = int(line_list[0])
            mac = line_list[1]
            port = line_list[3]
            if int(vl) == vlan:
                entries.append((vlan, mac, port))
for vlan, mac, port in sorted(entries):
    print(f'{vlan:<4}     {mac}      {port}')
