import os, path
import platform

Current_dir = os.getcwd()
history = []
while True:
    print('Текущая папка:' + Current_dir)
    print('1. пополнение счета')
    print('2. информация об ОС')
    print('l. просмотр содержимого рабочей директории;')
    print("d.посмотреть только папки;")
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

        print(platform.release())
    elif choice == '7':
        print('Викторина!')
    elif choice == '8':
        print('Банковский счет!')
    elif choice == 'l':
        print(os.listdir())
    elif choice == 'd':
        for d in os.listdir(os.getcwd()):
            if os.path.isdir(d):
                print('dir::::::::::::::::::::::::::::',d)
    elif choice == 'f':
        for d in os.listdir(os.getcwd()):
            if os.path.isfile(d):
                print('file::::::::::::::::::::::::::::',d)




    elif choice == '3':
        print(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')