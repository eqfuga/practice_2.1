from datetime import datetime

log_file = "calculator.log"
1
try:
    with open(log_file, 'r') as f:
        lines = f.readlines()
        print("\nПоследние 5 операций:")
        for line in lines[-5:]:
            print(line.strip())
except:
    print("Файл лога пока пуст")

while True:
    print("\n1. Калькулятор")
    print("2. Очистить лог")
    print("3. Выход")
    
    choice = input("Выбери: ")
    
    if choice == "1":
        try:
            a = float(input("Первое число: "))
            b = float(input("Второе число: "))
            op = input("Операция (+, -, *, /): ")
            
            if op == "+":
                res = a + b
            elif op == "-":
                res = a - b
            elif op == "*":
                res = a * b
            elif op == "/":
                if b == 0:
                    print("На ноль делить нельзя!")
                    continue
                res = a / b
            else:
                print("Неверная операция")
                continue
                
            print(f"= {res}")
            
            with open(log_file, 'a') as f:
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{time}] {a} {op} {b} = {res}\n")
                
        except:
            print("Ошибка! Введите числа правильно")
            
    elif choice == "2":
        try:
            open(log_file, 'w').close()
            print("Лог очищен")
        except:
            print("Ошибка")
            
    elif choice == "3":
        print("Пока!")
        break
    else:
        print("Неверный выбор")