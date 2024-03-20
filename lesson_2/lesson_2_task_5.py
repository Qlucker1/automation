def month_to_season(m):
    if m > 0 and m < 4:
        print ("Зима")
    elif m > 3 and m < 8:
        print ("Весна")
    elif m > 8 and m < 11:
        print ("Осень")
    else:
        print ("Лето")
try:
    month_to_season(m= int(input("Введите номер месяца: ")))
except ValueError:
    print("Вводите только числа!")