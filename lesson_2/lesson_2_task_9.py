var_1 = 37
var_2 = 99

def swap(var_1, var_2):
    a = var_1
    var_1 = var_2
    var_2 = a
    return var_1, var_2

res = swap(var_1, var_2)
print("Вар 1", res[0])
print("Вар 2", res[1])
