import re

input_string = input("Введите строку текста: ")
numbers = re.findall(r'\d+', input_string)
if numbers:
    print("Числа, найденные в строке:")
    for number in numbers:
        print(number)
else:
    print("Числа не найдены в строке.")