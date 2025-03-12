# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]
in_file = argv[1]
out_file = argv[2]

with open(in_file, 'r') as f:
    for line in f:
        if line.startswith('!'):
            continue
        elif ignore[0] in line:
            continue
        elif ignore[1] in line:
            continue
        elif ignore[2] in line:
            continue
        # print(line.rstrip())
        write = open(out_file, 'a')
        write.write(line)
        write.close()