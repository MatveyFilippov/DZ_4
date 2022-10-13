input("Чтобы начать нажмите ENTER")
print()
SIZE= int(input("Введите размер масива: "))
ARRAY = [0] * SIZE
print()
print("Выберите  K  если хотите ввести элементы с клавиатуры" )
print("Выберите  R  если хотите, чтоб элементы были сгенерированы рандомно в диапозоне от -999999 до 999999" )
CHOICE = input("Введите K или R: ")
while CHOICE != "K" and CHOICE != "R":
    CHOICE = input("Ошибка! Введите заглавные Y или R: ")
else:
    print("Хорошо!")
    print()
    if CHOICE == "K":
        for i in range(SIZE):
            print("Введите элемент №", i + 1,":", sep="", end=" ")
            ARRAY[i] = float(input())
    else:
        from random import randint
        for i in range(SIZE):
            ARRAY[i] = randint(-999999, 999999)
print()
input("Нажмите ENTER чтобы проверить верность полученных данных")
print()
print("Размера массива:", SIZE)
print("Ваш массив:", ARRAY)
print()
input("Если всё верно нажмите ENTER")
print()
