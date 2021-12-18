string = input("Введіть строку: ")
n = string.count("а")
n2 = string.count("А")

print("Нова строка -> ", string.replace("а", "о").replace("А", "О"))
print("Кількість замін: ", n+n2)