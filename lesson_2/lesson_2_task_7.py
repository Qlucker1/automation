a = 0
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
new_lst = []
for i in lst:
    a += i
new_lst.insert(0,a)
print('Сумма всех чисел списка равна: ', new_lst[-1])