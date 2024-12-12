# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input(f"Введите IP-адрес в формате 10.0.1.1: ")



try:
    ip_list = ip.split('.')
    flag = False
    if len(ip_list) != 4:
        raise ValueError("Неправильный IP-адрес")

    for i in ip_list:
        if not i.isnumeric() or int(i) not in range(0,256):
            print("Неправильный IP-адрес")
            flag = True
            break

    if flag == False:
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

except ValueError:
    print("Неправильный IP-адрес")
