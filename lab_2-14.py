from random import randint

first_list = [randint(1,100) for i in range(10)]
second_list = [randint(1,100) for i in range(10)]

print(first_list)
print(second_list)

print("Об'єднуємо та сортуємо масиви:")
sorted_list = sorted(first_list + second_list)

print(sorted_list)