# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input(f"Введите IP-адрес в формате 10.0.1.1: ")
ip_correct = False

while not ip_correct:
    ip_list = ip.split('.')
    flag = False

    if len(ip_list) != 4:
        print("Неправильный IP-адрес")
        flag = True


    for i in ip_list:
        if not i.isnumeric() or int(i) not in range(0,256):
            print("Неправильный IP-адрес")
            flag = True
            break

    if flag == False:
        ip_correct = True
        broadcast = '255.255.255.255'
        first_byte = int(ip.split('.')[0])
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
        break

    ip = input(f"Введите IP-адрес в формате 10.0.1.1: ")
