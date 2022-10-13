input("Чтобы начать нажмите ENTER")
print()
SIZEA = int(input("Введите размер масива A: "))
ARRAYA = [0] * SIZEA
SIZEB = int(input("Введите размер масива B: "))
ARRAYB = [0] * SIZEB
print()
print("Выберите  K  если хотите ввести элементы для массива A с клавиатуры" )
print("Выберите  R  если хотите, чтоб элементы для массива A были сгенерированы рандомно в диапозоне от -999999 до 999999" )
CHOICEA = input("Введите K или R: ")
while CHOICEA != "K" and CHOICEA != "R":
    CHOICEA = input("Ошибка! Введите заглавные K или R: ")
else:
    if CHOICEA == "K":
        print("Хорошо!")
        print()
        for i in range(SIZEA):
            print("Введите элемент №", i + 1,":", sep="", end=" ")
            ARRAYA[i] = float(input())
    else:
        from random import randint
        for i in range(SIZEA):
            ARRAYA[i] = randint(-999999, 999999)
print()
print("Выберите  K  если хотите ввести элементы для массива B с клавиатуры" )
print("Выберите  R  если хотите, чтоб элементы для массива B были сгенерированы рандомно в диапозоне от -999999 до 999999" )
CHOICEB = input("Введите K или R: ")
while CHOICEB != "K" and CHOICEB != "R":
    CHOICEB = input("Ошибка! Введите заглавные K или R: ")
else:
    if CHOICEB == "K":
        print("Хорошо!")
        print()
        for i in range(SIZEB):
            print("Введите элемент №", i + 1,":", sep="", end=" ")
            ARRAYB[i] = float(input())
    else:
        from random import randint
        for i in range(SIZEB):
            ARRAYB[i] = randint(-999999, 999999)
print()
print("Принято! Сверьтесь всё ли верно?")
print()
print("Размера массива A:", SIZEA)
print("Mассив A:", ARRAYA)
print()
print("Размера массива B:", SIZEB)
print("Mассив B:", ARRAYB)
print()
input("Нажмите ENTER")
if ARRAYA[i] == ARRAYB[i]:
    X = i
    ARRAYN = [0] * X
    print(ARRAYN)
else:
    print("Нет общих элементов")