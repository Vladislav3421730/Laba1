
jewelry_store = {
    'Кольцо': ['Золото', 1000, 10],
    'Серьги': ['Серебро', 500, 15],
    'Браслет': ['Золото', 800, 5],
    'Подвеска': ['Золото', 1200, 8],
    'Часы': ['Сталь', 300, 20]
}


def view_description():
    for item, description in jewelry_store.items():
        print(f'{item} - {description[0]}')


def view_prices():
    for item, description in jewelry_store.items():
        print(f'{item} - {description[1]}')


def view_quantities():
    for item, description in jewelry_store.items():
        print(f'{item} - {description[2]}')

def view_all_info():
    for item, description in jewelry_store.items():
        print(f'{item}: Материал - {description[0]}, Цена - {description[1]}, Количество - {description[2]}')

def buy_product():
    ListOfProduct=list()
    ListOfNums=list()
    ListOfCost=list()
    while True:
        item = input("Введите название товара (или 'n' для завершения покупки): ")
        if item == 'n':
            break
        if item in jewelry_store:
            try:
                quantity = int(input(f"Введите количество для покупки товара '{item}': "))
                if quantity>= jewelry_store[item][2]:
                        print(f"Извините,  недостаточно товара '{item}' в магазине.")
                else:
                    if 1 > quantity:
                        quantity = int(input("Введите нормальное количество товара : "))
                    ListOfProduct.append(item)
                    ListOfNums.append(quantity)
                    ListOfCost.append(jewelry_store[item][1]*quantity)
                    jewelry_store[item][2] -= quantity
            except ValueError:
                print("Пожалуйста, введите корректное количество.")
        else:
            print("Такого товара нет в магазине.")
    if(sum(ListOfCost)):
            print("Ваш чек")
            for product,num,cost in zip(ListOfProduct,ListOfNums,ListOfCost):
                    print(f"{product},{num} штук. , за всё : {cost}")
            print(f"Общая сумма покупки : {sum(ListOfCost)}")
def add_item():
    item = input("Введите название нового товара: ")
    if item in jewelry_store:
        print("Такой товар уже существует в магазине.")
    else:
        material = input(f"Введите материал для товара '{item}': ")
        try:
            price = int(input(f"Введите цену для товара '{item}': "))
            quantity = int(input(f"Введите количество для товара '{item}': "))
            jewelry_store[item] = [material, price, quantity]
            print(f"Товар '{item}' добавлен в магазин.")
        except ValueError:
            print("Пожалуйста, введите корректные данные.")


while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цен")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Добавить товар")
    print("7. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        view_description()
    elif choice == '2':
        view_prices()
    elif choice == '3':
        view_quantities()
    elif choice == '4':
        view_all_info()
    elif choice == '5':
        buy_product()
    elif choice == '6':
        add_item()
    elif choice == '7':
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите пункт меню от 1 до 6.")
