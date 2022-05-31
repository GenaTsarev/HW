from random import randint

num = randint(1, 100)
guess = 0
attempts = 0

while guess != num:
    guess = int(input('Введите число'))
    attempts += 1
    if guess > num:
        print('Загаданое число меньше')
    elif guess < num:
        print('Загаданое число больше')
print('Вы отгадали число! Отгадали с ', attempts, 'попыток')
