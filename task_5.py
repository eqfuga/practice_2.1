import json

file = "library.json"

try:
    with open(file, 'r'):
        pass
except:
    with open(file, 'w') as f:
        json.dump([], f)

def load():
    with open(file, 'r') as f:
        return json.load(f)

def save(data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)

def show():
    books = load()
    if not books:
        print("Нет книг")
        return
    print("\nВсе книги:")
    for b in books:
        status = "есть" if b['available'] else "нет"
        print(f"{b['id']}. {b['title']} - {b['author']} ({b['year']}) - {status}")

def search():
    books = load()
    word = input("Что ищем? ").lower()
    found = False
    for b in books:
        if word in b['title'].lower() or word in b['author'].lower():
            print(f"{b['title']} - {b['author']} ({b['year']})")
            found = True
    if not found:
        print("Ничего нет")

def add():
    books = load()
    
    if books:
        new_id = max(b['id'] for b in books) + 1
    else:
        new_id = 1
    
    title = input("Название: ")
    author = input("Автор: ")
    try:
        year = int(input("Год: "))
    except:
        print("Год должен быть числом")
        return
    
    books.append({
        'id': new_id,
        'title': title,
        'author': author,
        'year': year,
        'available': True
    })
    
    save(books)
    print("Книга добавлена!")

def status():
    books = load()
    try:
        id = int(input("ID книги: "))
    except:
        print("Ошибка")
        return
    
    for b in books:
        if b['id'] == id:
            b['available'] = not b['available']
            save(books)
            print("Статус изменен")
            return
    print("Не найдено")

def delete():
    books = load()
    try:
        id = int(input("ID книги для удаления: "))
    except:
        print("Ошибка")
        return
    
    for i in range(len(books)):
        if books[i]['id'] == id:
            del books[i]
            save(books)
            print("Удалено")
            return
    print("Не найдено")

def export():
    books = load()
    available = []
    for b in books:
        if b['available']:
            available.append(b)
    
    with open('available.txt', 'w') as f:
        for b in available:
            f.write(f"{b['title']} - {b['author']} ({b['year']})\n")
    
    print(f"Сохранено {len(available)} книг")

while True:
    print("\nМеню:")
    print("1. Показать все")
    print("2. Поиск")
    print("3. Добавить")
    print("4. Статус (взята/вернули)")
    print("5. Удалить")
    print("6. Экспорт доступных")
    print("7. Выход")
    
    choice = input("Выбери: ")
    
    if choice == "1":
        show()
    elif choice == "2":
        search()
    elif choice == "3":
        add()
    elif choice == "4":
        status()
    elif choice == "5":
        delete()
    elif choice == "6":
        export()
    elif choice == "7":
        print("Пока!")
        break
    else:
        print("Неверно, выбери 1-7")