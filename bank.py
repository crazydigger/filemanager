# """
# МОДУЛЬ 3
# Программа "Личный счет"
# Описание работы программы:
# Пользователь запускает программу у него на счету 0
# Программа предлагает следующие варианты действий
# 1. пополнить счет
# 2. покупка
# 3. история покупок
# 4. выход
# 1. пополнение счета
# при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
# после того как пользователь вводит сумму она добавляется к счету
# снова попадаем в основное меню
# 2. покупка
# при выборе этого пункта пользователю предлагается ввести сумму покупки
# если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
# если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
# снимаем деньги со счета
# сохраняем покупку в историю
# выходим в основное меню
# 3. история покупок
# выводим историю покупок пользователя (название и сумму)
# возвращаемся в основное меню
# 4. выход
# выход из программы
# При выполнении задания можно пользоваться любыми средствами
# Для реализации основного меню можно использовать пример ниже или написать свой
import os.path
import pickle


def bank():
    Account = 0
    history = []
    if os.path.exists('account.txt'):
        with open('account.txt', 'rt') as file:
            Account = int(file.read())
            print('увас' + str(Account) + 'руб!')
            if Account == 0:
                print('пополните счет!!!!!!')
    # else:
    with open('acount.txt', 'at') as file:
        file.writelines(str(Account))

    if os.path.exists('history.txt'):
        print('найдена история покупок!загружаем!')
        f = open('history.txt', 'rt', encoding='utf8')
        for l in f:
            print(l)
            history.append(l)
    while True:
        print('денег на счету:', Account)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            sum = input('на сколько пополнить счет')
            Account += int(sum)
        elif choice == '2':
            sum = int(input('стоимость покупки?'))
            if (sum <= Account):
                print('Денег достаточно')
                good = input('название товара?')
                history.append(good + ',' + str(sum))
                break
            else:
                print('недостаточно средств!')
                break
                good = input('название товара?')
                history.append(good + ',' + str(sum))
        elif choice == '3':
            if len(history) == 0:
                print('не было покупок!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print(history)
        elif choice == '4':
            with open('account.txt', 'wt') as file:
                file.writelines(str(Account))
                with open('history.txt', 'at', encoding='utf8') as file:
                    for l in history:
                        print(l)
                        file.write(l + '\n')
            break
        else:
            print('Неверный пункт меню')
