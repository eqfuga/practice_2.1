import csv

try:
    with open('products.csv', 'r'):
        pass
except:
    with open('products.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Название', 'Цена', 'Количество'])
        writer.writerow(['Яблоки', 100, 50])
        writer.writerow(['Бананы', 80, 30])
        writer.writerow(['Молоко', 120, 20])
        writer.writerow(['Хлеб', 40, 100])
    print("Файл создан!")

tovary = []
with open('products.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row:
            tovary.append([row[0], int(row[1]), int(row[2])])

def show_tovary():
    print("\nТовары:")
    for t in tovary:
        print(f"{t[0]} - {t[1]} руб. - {t[2]} шт. = {t[1]*t[2]} руб.")

def add_tovar():
    name = input("Название товара: ")
    try:
        price = int(input("Цена: "))
        kol = int(input("Количество: "))
        if price <= 0 or kol <= 0:
            print("Ошибка! Числа должны быть больше 0")
            return
        tovary.append([name, price, kol])
        print("Товар добавлен!")
    except:
        print("Ошибка! Введите числа правильно")

def search_tovar():
    poisk = input("Что ищем? ").lower()
    for t in tovary:
        if t[0].lower() == poisk:
            print(f"{t[0]}, цена {t[1]}, количество {t[2]}")
            return
    print("Такого товара нет(")

def total_cost():
    summ = 0
    for t in tovary:
        summ += t[1] * t[2]
    print(f"Общая стоимость склада: {summ} руб.")

def save_to_file():
    with open('products.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Название', 'Цена', 'Количество'])
        for t in tovary:
            writer.writerow([t[0], t[1], t[2]])
    print("Сохранено в файл!")

while True:
    print("\n1 - Показать все товары")
    print("2 - Добавить товар")
    print("3 - Найти товар")
    print("4 - Посчитать стоимость всего")
    print("5 - Сохранить в файл")
    print("6 - Выход")
    
    vibor = input("Введи номер: ")
    
    if vibor == "1":
        show_tovary()
    elif vibor == "2":
        add_tovar()
    elif vibor == "3":
        search_tovar()
    elif vibor == "4":
        total_cost()
    elif vibor == "5":
        save_to_file()
    elif vibor == "6":
        break
    else:
        print("Неправильно, выбери от 1 до 6")