def square(a):
    S = a**2
    if type(S) is int:
        print(S)
    elif type(S) is float:
        print(round(S))

square(a= float(input('Введите число: ')))