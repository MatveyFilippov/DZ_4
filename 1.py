input("Чтобы начать нажмите ENTER")
print()
M = int(input("Введите размер масива: "))
B = [0] * M
print()
print("Выберите  Y  если хотите ввести элементы с клавиатуры" )
print("Выберите  R  если хотите, чтоб элементы были сгенерированы рандомно в диапозоне от -999999 до 999999" )
V = input("Введите Y или R: ")
while V != "Y" and V != "R":
    V = input("Ошибка! Введите заглавные Y или R: ")
else:
    print("Хорошо!")
    if V == "Y":
        for i in range(M):
            print("Введите элемент №", i + 1,":", sep="", end=" ")
            B[i] = float(input())
    else:
        from random import randint
        for i in range(M):
            B[i] = float(randint(-999999, 999999))
print()
input("Нажмите ENTER чтобы проверить верность полученных данных")
print()
print("Размера массива:", M)
print("Ваш массив:", B)
print()
input("Если всё верно нажмите ENTER")
