input_str = input("Введите список целых чисел через пробел: ")
try:
    numbers = [int(x) for x in input_str.split()]
except ValueError:
    print("Ошибка: Введите только целые числа, разделенные пробелами.")
    exit()

try:
    C = int(input("Введите значение C: "))
except ValueError:
    print("Ошибка: Введите целое число для значения C.")
    exit()
count_more_than_C=0
for i in range(0,len(numbers)):
        if numbers[i]>C:
                count_more_than_C=count_more_than_C+1
print("Количество элементов больше чем ",C," : ",count_more_than_C)
max_module_number=numbers[0];
for i in range(0,len(numbers)):
        if max_module_number<numbers[i]:
                max_module_number=numbers[i]
                max_abs_index =i

if max_abs_index < len(numbers) - 1:
    product_after_max = 1
    for i in range(max_abs_index+1,len(numbers)):
            product_after_max=product_after_max*numbers[i]
    print("Произведение элементов после максимального по модулю элемента:", product_after_max)
else:
        print("Максимальный по модулю элемент был последним")

positive_numbers = [x for x in numbers if x > 0]
for num in positive_numbers:
    while num in numbers:
        numbers.remove(num)
print("Список после удаления положительных элементов:", numbers)

