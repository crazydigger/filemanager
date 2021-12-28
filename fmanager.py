import os
import platform

Current_dir = os.getcwd()
history = []
while True:
    print('Текущая папка:' + Current_dir)
    print('1. пополнение счета')
    print('2. информацияоб ОС')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        sum = input('на сколько пополнить счет')
        Account += int(sum)
    elif choice == '2':
        print(platform.system())

        print(platform.release())




    elif choice == '3':
        print(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')