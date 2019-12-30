# Напишите функцию где дан список целых чисел. Заменить отрицательные на -1,
# положительные - на число 1, ноль оставить без изменений.

num = [5, -5, 6, 0, -1, 2, -3]
num2 = [] 
# for x in num:
#     if x < 0:
#         print(-1)
#     elif x > 0:
#         print(1)
#     else:
#         print(0)        

for x in num:
    if x > 0:
        num2.append(1)
    elif x < 0:
        num2.append(-1)
    else:
        num2.append(0)    
print(num,num2)        