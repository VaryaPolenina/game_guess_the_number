import random

def guess_the_number():
    secretik = random.randint(1, 100)
    popitka = 0
    max_popitka = 10

    print("Привет, добро пожаловать в игру 'Угадай число'!")
    print(f"Я уже загадал число от 1 до 100. У тебя {max_popitka} попыток.")

    while popitka < max_popitka:
        try:
            predpolozhenie = int(input(f"Твоя {popitka + 1} попытка. Твое предположение: "))
        except ValueError:
            print("Пожалуйста, введи целое число.")
            continue

        popitka += 1

        if predpolozhenie < secretik:
            print("Твое число меньше загаданного.")
        elif predpolozhenie > secretik:
            print("Твое число больше загаданного.")
        else:
            print(f"Поздравляю, ты угадал число! Загаданное число было: {secretik}.")
            break
    else:
        print(f"К сожалению, ты использовал все попытки. Загаданное число было: {secretik}. Удачи в следующий раз!")

    print("\nДля повторной игры нажми на любую клавишу.")
    input()
    guess_the_number()


guess_the_number()
