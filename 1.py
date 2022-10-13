input("Чтобы начать нажмите ENTER")
print()
SIZE = int(input("Введите размер масива: "))
ARRAY = [0] * SIZE
print()
print("Выберите  K  если хотите ввести элементы с клавиатуры" )
print("Выберите  R  если хотите, чтоб элементы были сгенерированы рандомно в диапозоне от -999999 до 999999" )
CHOICE = input("Введите K или R: ")
while CHOICE != "K" and CHOICE != "R":
    CHOICE = input("Ошибка! Введите заглавные K или R: ")
else:
    if CHOICE == "K":
        print("Хорошо!")
        print()
        for i in range(SIZE):
            print("Введите элемент №", i + 1,":", sep="", end=" ")
            ARRAY[i] = float(input())
    else:
        from random import uniform
        for i in range(SIZE):
            ARRAY[i] = uniform(-999999, 999999)
print("Принято! Сверьтесь всё ли верно?")
print()
print("Размера массива:", SIZE)
print("Ваш массив:", ARRAY)
print()
input("Нажмите ENTER")
IMAX = 0
for i in range(SIZE):
    if ARRAY[i] > ARRAY[IMAX]:
        IMAX = i

ARRAY[IMAX + 1: len(ARRAY)] = [0] * (SIZE - 1 - IMAX)
print("Полученный массив:", ARRAY)
print()
input("Чтобы завершить нажмите ENTER")