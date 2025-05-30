# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input(f"Введите IP-адрес в формате 10.0.1.1: ")
first_byte = int(ip.split('.')[0])
broadcast = '255.255.255.255'

if 0 < first_byte < 224:
    print ('unicast')
elif 223 < first_byte < 240:
    print('multicast')
elif ip == broadcast:
    print('local broadcast')
elif ip == '0.0.0.0':
    print ('unassigned')
else:
    print ('unused')