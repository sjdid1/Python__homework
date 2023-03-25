# Задача 26:  Напишите программу, которая 
# на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def exponent(numb, exp):
    if (exp == 1):
        return (numb)
    if (exp != 1):
        return (numb * exponent(numb, exp - 1))
numb = int(input("Введите A: "))
exp = int(input("Введите B: "))
print(f'A = {numb}; B = {exp} -> {exponent(numb, exp)}')
