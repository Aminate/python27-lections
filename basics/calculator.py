num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
operation = input('Выберите операцию из следующих \n\t #+-*/%**// : ')
if operation in ('+', '-', '*', '/', '**', '%', '//'):
    if operation == '+':
        print(num1+num2)
    elif operation == '-':
        print(num1-num2)
    elif operation == '*':
        print(num1*num2)
    elif operation == '/':
        try:
            print(num1/num2)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        else:
            print(num1/num2)
    elif operation == '**':
        print(num1**num2)
    elif operation == '%':
        try:
            print(num1%num2)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        else:
            print(num1%num2)
    elif operation == '//':
        try:
            print(num1//num2)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
else:
    print("Данной операции нет в системе")






















