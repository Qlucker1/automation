def bank(x, y):
    balance = x
    for x in range(y):
        new_balance = balance + balance * (0.1 *y) 
        return new_balance
try:
    x = int(input("Какую сумму вы хотите положить? \n Введите значение: "))
    y = int(input('На какой срок желаете вложить? \n Введите значение: '))
except ValueError:
    print('Вводите только числа!')
print(bank(x, y))