number_list = [i for i in range(35, 87+1)]

result = [t for t in number_list if t%7 in [1,2,5]]

print("Числа що відаовідають заданому критерію: ")
print(result)

