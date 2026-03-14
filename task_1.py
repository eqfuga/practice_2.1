print("Введите 5 строк текста:")
lines = []

for i in range(5):
    line = input(f"Строка {i+1}: ")
    lines.append(line)

with open('text.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line + '\n')

with open('text.txt', 'r', encoding='utf-8') as f:
    content = [line.strip() for line in f.readlines()]
    
    print("\nРЕЗУЛЬТАТЫ АНАЛИЗА:")
    print(f"• Строк в файле: {len(content)}")
    
    total_words = sum(len(line.split()) for line in content)
    print(f"• Слов в файле: {total_words}")
    
    longest = max(content, key=len)
    print(f"• Самая длинная строка ({len(longest)} симв.):")
    print(f"  {longest}")