n = 1

num_list = [int(input("Введіть елемент №"+ str(i+1) + " : ")) for i in range(10+n)]

print("Введений масив: ", num_list)
print("Максиамльний елемент маисву: ", max(num_list))
print("Реверсивний масив: ", num_list[::-1])