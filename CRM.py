import calendar
import datetime

clients = {}
try:
    file = open('fusk1.txt', 'r')
except: 
    print('file not found')
else:
    date = ''
    time = ''
    name = ''
    surname = ''
    identity = ''
    for line in file:
        if 'date' in line:
            date = line[6:-1]
        elif 'time' in line:
            time = line[6:-1]
        elif 'client' in line:
            # print(line)
            identity = line[8:-1]
            #print(identity)
            identity = identity.split()
            name = identity[0]
            surname = identity[1]
        clients[date] = {time : [name , surname]}

datenow = datetime.datetime.now()
flag = True
def stopwork(usersinput):
    if usersinput.lower() == 'finish':
        return False
    else:
        return True
def errorname(): 
    while True:
        person = input('Введите фамилию и имя: ').title().split()
        personcheck = stopwork(person[0])
        if personcheck == False:
            return False  
        else:
            if len(person) != 2:
                print('Ошибка! Введите фамилию и имя')
                continue
            elif person[0].isalpha() and person[1].isalpha():
                return person
                
def checkint(i):
    try:
        i = int(i)
        if i != 0:
            return i
        else:
            print('Ошибка! Введите число больше 0')
            return False
    except: 
        print('Ошибка! Введите число')
        return False
def checkdata(a):
    if not a:
        return True
    else:
        return False
def correctyear():
    global datenow
    year = 'dfgjt'
    currentyear = 0
    while currentyear < datenow.year or len(year) != 4:
        year = input('Введите год: ')
        finishyear = stopwork(year)
        if  finishyear == False:
            return False
        else:
            currentyear = checkint(year)
            if len(year) != 4 or currentyear < datenow.year:
                print('Неверно указали год или(и) ввели меньше 4 цифр, попробуйте еще')
    return currentyear
def correctmonth():
    global bookyear
    while True:
        month = input('Введите месяц: ')
        finishmonth = stopwork(month)
        if finishmonth == False:
            return False
        else:
            currentmonth= checkint(month)
            if  currentmonth > 12 or currentmonth < 1:
                print('некорректный ввод, введите число от 1 до 12: ')
                continue
            elif currentmonth < datenow.month and currentyear == datenow.year:
                print('некорректный ввод, попробуйте еще раз')
            elif currentmonth >= datenow.month or currentyear > datenow.year:
                break
    return currentmonth

def correctday():
    global bookyear, bookmonth
    while True:
        day = input('Введите день: ')
        finishday = stopwork(day)
        if finishday == False:
            return False
        else:
            day = abs(checkint(day)) 
            if bookmonth == datenow.month:
                if  day < datenow.day:
                    print('некорректно введен день, попробуйте еще раз')
                    continue
            elif bookmonth > datenow.month and bookyear == datenow.year or bookyear > datenow.year:
                day = day
            if (bookmonth < 8 and bookmonth % 2 == 1) or (bookmonth >= 8 and bookmonth % 2 == 0):
                if day > 31:
                    print('Некорректно введен день, попробуйте еще: ')
                    continue
            elif (bookyear % 4 == 0 and bookyear % 100 != 0) or bookyear % 400 == 0 and bookmonth == 2:
                if day > 29:
                    print('Некорректно введен день, попробуйте еще: ')
                    continue
            elif bookmonth == 2 and day > 28:
                print('Некорректно введен день, попробуйте еще: ')
                continue
            elif day > 30:
                print('Некорректно введен день, попробуйте еще: ')
                continue
            weekday = calendar.weekday(bookyear, bookmonth, day)
            if weekday == 0 or weekday == 1:
                print('Данный день является выходным, введите другой день записи: ')
                continue
            else:
                break
    return day

currentyear = correctyear()
currentmonth = correctmonth()
calendar.prmonth(currentyear,currentmonth)

while True:
    bookyear = correctyear()
    if bookyear == False:
        break
    bookmonth = correctmonth()
    if bookmonth == False:
        break
    bookday = correctday()
    if bookday == False:
        break
    bookperson = errorname()
    if bookperson == False:
        break
    booktime = input('введите время  через двоеточие: ')
    date = str(bookday) + '.' + str(bookmonth) + '.' + str(bookyear)
    if date in clients:
        print('время занято')
    else:
        clients[date] = {booktime : bookperson}
        

with open ('fusk1.txt', 'w', encoding='UTF-8') as file: 
    for i in clients:
        file.write('date: ') 
        file.write(i)
        file.write('\n')
        for j in clients[i]:
            file.write('time: ')
            file.write(j)
            file.write('\n')
            file.write('client: ')
            for c in clients[i][j]:
                file.write(c)
                file.write(' ')
        file.write('\n')
        file.write('\n')