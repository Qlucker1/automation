def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end="\n")
        elif i % 3 == 0:
            print('Fizz', end='\n')
        elif i % 5 == 0:
            print('Buzz', end='\n')
        else:
            print(i, end='\n')

fizz_buzz(n= int(input('Введите число: ')))