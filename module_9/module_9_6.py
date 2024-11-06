

def all_variants(text):
    length = len(text)
    for x in range(1, length + 1):
        for y in range(length - x + 1):
            yield text[y:y + x]

a = all_variants("abc")
for i in a:
    print(i)


