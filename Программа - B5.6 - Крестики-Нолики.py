print()
print('Приветствуем Вас в игре "Крестики-Нолики"!')
print()

# Определяем базовые функции
def ViborSimvola():
    print('В игру играют 2 человека. Пускай игрок, который будет делать первый ход, выберет себе символ, который он будет использовать на протяжении игры.')
    Simvol = input('Символ первого игрока (укажите "1" для "Х" или "2" для "0"): ')
    Simvoli = ['X', '0']
    if Simvol == '1':
        Igrok1 = Simvoli[0]
        Igrok2 = Simvoli[1]
    elif Simvol == '2':
        Igrok1 = Simvoli[1]
        Igrok2 = Simvoli[0]
    else:
        print('Введенно неверное значение, попробуйте еще раз.')
        return ViborSimvola()

    Itog=((1,Igrok1), (2,Igrok2))

    print()
    print('Выбор сделан!')
    print(f'Игрок №{Itog[0][0]} - ', Itog[0][1])
    print(f'Игрок №{Itog[1][0]} - ', Itog[1][1])
    print()
    print('---')

    return Itog

def Pole_Vid(Pole):
    print()
    print('Игровое поле:')
    print(' |-----|-----|-----|')
    print('', '|', Pole[0], '|', Pole[1], '|', Pole[2], '|')
    print(' |-----|-----|-----|')
    print('', '|', Pole[3], '|', Pole[4], '|', Pole[5], '|')
    print(' |-----|-----|-----|')
    print('', '|', Pole[6], '|', Pole[7], '|', Pole[8], '|')
    print(' |-----|-----|-----|')
    print()

def Proverka(Simvoli,Pole,NomerIgroka):
    Igrok=Simvoli[NomerIgroka-1]
    Nomer=Igrok[0]
    Simvol=Igrok[1]

    Stroki=[Pole[0:3],Pole[3:6],Pole[6:9]]
    Stolbci=[[Pole[0+3*i] for i in range(0,3)],[Pole[1+3*i] for i in range(0,3)],[Pole[2+3*i] for i in range(0,3)]]
    Dianonali=[[Pole[0],Pole[4],Pole[8]],[Pole[2],Pole[4],Pole[6]]]
    VseKombinacii=Stroki+Stolbci+Dianonali

    # Проверка выигрышных комбинаций
    for Kombinacia in VseKombinacii:
        if Kombinacia[0]==Kombinacia[1] and Kombinacia[0]==Kombinacia[2]:
            print('---')
            print('ИГРА ЗАВЕРШЕНА')
            Pole_Vid(Pole)
            print(f'Игрок №{Nomer} ("{Simvol}") победил!')
            Dalee()
            return 0

    # Проверка на ничью
    StopFaktor=0
    for Kombinacia in VseKombinacii:
        if (' '+Simvoli[0][1]+' ') in Kombinacia and (' '+Simvoli[1][1]+' ') in Kombinacia:
            StopFaktor+=1
    if StopFaktor==8:
        print('---')
        print('ИГРА ЗАВЕРШЕНА')
        Pole_Vid(Pole)
        print(f'Объявлена ничья!')
        Dalee()
        return 0
    else:
        return 1

def Hod(Simvoli,Pole,NomerIgroka):
    Igrok=Simvoli[NomerIgroka-1]
    Nomer=Igrok[0]
    Simvol=Igrok[1]

    print(f'Ход игрока №{Nomer} ("{Simvol}"):')

    Pole_Vid(Pole)

    Mesto=input('Введите номер поля, куда хотите поместить Ваш символ: ')
    print()

    if Mesto.isdigit() and int(Mesto)>=1 and int(Mesto)<=9:
        print()
        Mesto=int(Mesto)-1
        if Pole[Mesto]!=(' '+Simvoli[0][1]+' ') and Pole[Mesto]!=(' '+Simvoli[1][1]+' '):
            Pole[Mesto]=' '+Simvol+' '
            Stop=Proverka(Simvoli, Pole, NomerIgroka)

            if Stop==0:
                return None
            else:
                if NomerIgroka==1:
                    NomerIgroka=2
                else:
                    NomerIgroka=1
        else:
            print('Введено некорректное поле, укажите номер свободного поля!')
            print()
    else:
        print('Введено некорректное поле, укажите номер свободного поля!')
        print()

    print('---')
    return Hod(Simvoli, Pole, NomerIgroka)


def Igra():
    # Выбор символов для игроков
    Simvoli=ViborSimvola()

    # Создание игрового поля
    Pole=[f'({i+1})' for i in range(0,9)]
    print()

    # Первый ход
    Hod(Simvoli,Pole,1)

def Dalee():
    print()
    print('Хотите продолжить?')
    Otvet=input('Введите "1" для перезапуска игры или "2" для выхода: ')
    print()

    if Otvet=='1':
        print('=====')
        Igra()
    else:
        print('Конец')
        return None

# Запуск игры
Igra()




