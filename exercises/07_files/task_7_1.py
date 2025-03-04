# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

f = open('ospf.txt')

for line in f:
    print(f'''
        Prefix                {line.strip().split(' ')[8]}
        AD/Metric             {line.strip().split(' ')[9].strip('[]')}
        Next-Hop              {line.strip().split(' ')[11].strip(',')}
        Last update           {line.strip().split(' ')[12].strip(',')}
        Outbound Interface    {line.strip().split(' ')[13]}

    ''')