# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input())
spisok = list(range(1, n + 1))
print(spisok)
x = int(input())
for i in range(0, len(spisok)):
    if x >= n:
        print(n)
        break 
else: print(x - 1)

        
        
    
        
    
    
print(f'->{x} ')

