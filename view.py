def inp_mod():
    mod = input('Выберете режим работы импорт или экспорт: ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname

def view_import (result):
    print(*result, sep='\n') 

def inp_export():
    surname = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    sec_name = input('Введите Отчество: ')
    phone = input('Введите номер телефона: ')
    comment = input('Ведите признак телефона (домашний, рабочий): ')
    return '\n', surname, name, sec_name, phone, comment


def view_import_no ():
    print(f'Данные не найдены')