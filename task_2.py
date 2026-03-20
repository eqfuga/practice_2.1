try:
    with open('students.txt', 'r'):
        pass
except FileNotFoundError:
    with open('students.txt', 'w', encoding='utf-8') as f:
        f.write("Иванов Иван:5,4,3,5\n")
        f.write("Петров Петр:4,3,4,4\n")
        f.write("Сидорова Мария:5,5,5,5\n")
        f.write("Чигур Антон:4,5,4,5\n")
        f.write("Джобс Стив:5,4,5,4\n")

students = []
averages = {}

with open('students.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            name, grades_str = line.split(':')
            grades = [int(g) for g in grades_str.split(',')]
            avg = sum(grades) / len(grades)
            averages[name] = avg
            students.append((name, grades, avg))

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write("Студенты со средним баллом > 4.0:\n\n")
    for name, grades, avg in students:
        if avg > 4.0:
            f.write(f"{name}: {avg:.2f} ({grades})\n")

best_student = max(averages.items(), key=lambda x: x[1])
print(f"Лучший студент: {best_student[0]} со средним баллом {best_student[1]:.2f}")
print("Результаты сохранены в файл result.txt")