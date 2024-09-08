def single_root_words(root_word, *other_words):
    some_words = []
    root_word = str(root_word).lower()
    for i in other_words:
        if root_word in str(i).lower():
            some_words.append(i)

    if len(some_words) == 0:
        for i in other_words:
            if str(i).lower() in root_word:
                some_words.append(i)

    return some_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)