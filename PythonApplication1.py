start = int(input("Початок діапазону: "))
end = int(input("Кiнець діапазону: "))

print("Усі числа діапазону:")
for num in range(start, end+1):
    print(num)

print("Усі числа діапазону за спаданням:")
for num in range(end, start-1, -1):
    print(num)

print("Усі числа, кратні 7:")
for num in range(start, end+1):
    if num % 7 == 0:
        print(num)

count = 0
for num in range(start, end+1):
    if num % 5 == 0:
        count += 1
print("Кількість чисел, кратних 5:", count)

