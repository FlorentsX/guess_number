from random import randint as rnd


x_number = rnd(1, 100)

print('Угадайте число от 1 до 100.')

while True:
    user_answer = int(input('Введите число: '))

    if user_answer > x_number:
        print('Загаданное число меньше')
    elif user_answer < x_number:
        print('Загаданное число больше')
    elif user_answer == x_number:
        break
    else:
        print('Вы ввесли некорректный ответ.')

print('Отличная интуиция! Вы угадали число :)')