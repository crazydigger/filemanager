import os, path
from path import *
import platform
import victory
import bank

Current_dir = os.getcwd()
history = []
Account = 0

def creator():
    print('создатель программы:Рома Боровиков(c)(r)')


while True:
    print('Текущая папка:' + Current_dir)
    creator()
    print('1. пополнение счета')
    print('2. информация об ОС')
    print('list. просмотр содержимого рабочей директории;')
    print("d.посмотреть только папки;")
    print("5.создатель программы;")
    print("remove.удалить (файл/папку);")
    print("C.reate.Создатьпапку);")
    print("f.посмотреть только файлы;")

    print('7.играть в викторину;')
    print('8.мой банковский счет;')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        sum = input('на сколько пополнить счет')
        Account += int(sum)
    elif choice == '2':
        print(platform.system())
    elif choice == '5':
       creator()
    elif choice == '7':
        print('Викторина!')
        victory.victorina()
    elif choice == '8':
        print('Банковский счет!')
        bank.bank()
    elif choice == 'l':
        print(os.listdir())
    elif choice == 'd':
        for d in os.listdir(os.getcwd()):
            if os.path.isdir(d):
                print('dir::::::::::::::::::::::::::::', d)
    elif choice == 'f':
        for d in os.listdir(os.getcwd()):
            if os.path.isfile(d):
                print('file::::::::::::::::::::::::::::', d)
    elif choice == 'r':

        f = input('введите имя файла или папки для удаления:')
        while input('1 - подтвердить 0- отменить') == '1':
            print('будет удален файл!!!!!!!!!!', f)
        if os.path.isdir(f):
            os.rmdir(f)
        else:
            os.remove(f)
    elif choice == 'c':

        f = input('введите имя файла или папки для Создания:')
        # while input('1 - подтвердить 0- отменить')=='1':
        # print('будет удален файл!!!!!!!!!!',f)
        # if os.path.isdir(f):
        os.mkdir(f)
        # else:
        #     os.remove(f)




    elif choice == '3':
        print(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
