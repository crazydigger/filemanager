import os, path
from path import *
#import platform
#import victory
#import bank
from bank import bank

Current_dir = os.getcwd()
history = []
Account = 0
choice='0'
def creator():
    return 'создатель программы:Рома Боровиков(c)(r)2022'
#choice=input('Выберите пункт меню')

creator()
while choice!='4':


    print('Текущая папка:' + Current_dir)
    print(creator())
    #print('1. пополнение счета')
    # print('2. информация об ОС')
    # print('list. просмотр содержимого рабочей директории;')
    # print("d.посмотреть только папки;")
    # print("5.создатель программы;")
    # print("remove.удалить (файл/папку);")
    # print("C.reate.Создатьпапку);")
    print("s. сохранить содержимое папки в файлlistdir.txt")

    #print('7.играть в викторину;')
    print('8.мой банковский счет;')
    print('4. выход')
    if __name__=='__main__':
        choice = input('Выберите пункт меню')

    if choice=='5':
        print(creator())


        print(os.listdir())

    if choice == 's':
        list=[]
        with open('listdir.txt','wt') as file:
            for d in os.listdir(os.getcwd()):


                if os.path.isfile(d):
                    file.write('file....' + d + '\n')
                    list.append(d)
                if os.path.isdir(d):
                    file.write('dir....' + d + '\n')
                    file.write(d + '\n')
                    list.append(d)
            file.writelines(list)
            print(list)

    if choice=='4':
        print('пока-пока!!')
#def test_creator():
    if choice=='8':
        print('Банковский счет!!')
        bank()
#