string = input("Введіть строку: ")

rev_string = string[::-1]

if(string == rev_string):
    print("Введена строка є паліндромом")
else:
    print("Введена строка не є паліндромом")