

def custom_write(file_name, strings):
    file = open(file_name, "w", encoding="utf-8")
    strings_positions = {}
    i = 1
    for s in strings:
        strings_positions[(i, file.tell())] = s
        file.write(f"{s}\n")
        i += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)