# -*- coding: cp1251 -*- 
start = int(input("Початок діапазону: "))
end = int(input("кінець діапазону: "))

for num in range(start, end+1):
    if num % 7 == 0:
        print(num)

