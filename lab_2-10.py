min = int(input("Ведіть мінімальне значення: "))
max = int(input("Веддіть максимальне значення: "))

sum = sum(i for i in range(min, max+1) if i % 2 != 0)
print("Сума парних чисел заданому діапазоні: ", sum )