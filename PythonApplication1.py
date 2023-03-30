start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

if start > end:
    start, end = end, start

for i in range(start, end+1):
    if i % 2 != 0:
        print(i)

