# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

Часть словаря, который должна возвращать функция (полный вывод можно посмотреть
в тесте test_task_9_4.py):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(config_filename):
    trunk_dict={}
    with open(config_filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if not line or ignore_command(line,ignore) or line.startswith('!'):
                continue
            if not line.startswith(' '):
                iface = line.rstrip()
                trunk_dict[iface] = []
            elif iface:
                vlan = line.strip()
                trunk_dict[iface].append(vlan)
    return trunk_dict

print(convert_config_to_dict('config_sw1.txt'))