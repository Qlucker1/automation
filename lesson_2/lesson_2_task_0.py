try:
    my_age = int(input('Введите ваш возраст: '))
    print ('Ваш возраст: ', my_age)
    my_age = my_age + 1
    print (' Через год вам будет: ', my_age)
except ValueError:
    print("Пожалуйста, вводите только числа")