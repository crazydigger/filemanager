from random import randint
import random
names = "а.с.пушкин,л.н.толстой,фмдостоевский,мюлермонтов,апчехов".split(',')
dates = '9.091928,28.081828,11111921,27061941,29011960'.split(',')
famous_persons={}
for i in range(len(names)):
    famous_persons=famous_persons.fromkeys(names)
    print(names[i],dates[i])
    n = names[i].replace('','')
    d = dates[i].replace('','')
    print('name!!!!!',n)
    print('date=====',d)
    famous_persons={n:d}
    #famous_persons(names[i],dates[i])
print(famous_persons)
def long_date(m):
    months={'01':'января','02':'февраля','03':'марта','04':'апреля','05':'мая','06':'июня','07':'июля','08':'августа','09':'сентября','10':'октября','11':'ноября','12':'декабря'}
    result=''
    try:
        result =months[m]
    except:
        result=''


    return result
for i in range(1,9):
        print(long_date('0'+str(i)))

while(input('повторим?-1нет-0')):
    for i in range(len(names)):
        famous_persons=famous_persons.fromkeys(names)
        print(names[i],dates[i])
        n = names[i].replace('','')
        d = dates[i].replace('','')
        print('name!!!!!',n)
        print('date=====',d)
        famous_persons={n:d}
        #famous_persons(names[i],dates[i])
    print(famous_persons)



    count_right=0
    for i in range(len(names)):








        d_answ=input('введите дату рождения'+names[i]+ 'в формате ddmmyyyy:')
        if(d_answ==dates[i]):

            print('right answer:',d_answ[:3]+long_date(d_answ[2:4])+d_answ[-4:])


            #print('месяц',long_date(d_answ[2:4]))
            count_right+=1
    print('gпроцент правильных ответов',round(count_right/len(names)*100,2))
    print('gпроцент неправильных ответов',100-round(count_right/len(names)*100,2))
