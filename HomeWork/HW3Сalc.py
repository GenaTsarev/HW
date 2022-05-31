num1 = int(input('Введите первое число '))
oper = input('Введите действие ')
num2 = int(input('Второе первое число '))

if oper == '+':
    print('Ответ', num1 + num2)
elif oper == '-':
    print('Ответ', num1 - num2)
elif oper == '*':
    print('Ответ', num1 * num2)
elif oper == "/":
    print('Ответ', num1 / num2)
else:
    print('Выбрано неправильное действие')