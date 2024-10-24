

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding="utf-8-sig") as file:
                file_words = []
                for line in file:
                    line = self.__remove_punctuation(line.lower())
                    for word in str.split(line):
                        file_words.append(word)
                all_words[name] = file_words
        return all_words

    def find(self, word):
        result = {}
        for key, value in self.get_all_words().items():
            for i, w in enumerate(value, start=1):
                if str.lower(w) == word.lower():
                    result[key] = i
                    break
        return result

    def count(self, word):
        result = {}
        for key, value in self.get_all_words().items():
            i = 0
            for w in value:
                if str.lower(w) == word.lower():
                    i += 1
            result[key] = i
        return result

    def __remove_punctuation(self, text):
        chars_to_remove = [',', '.', '=', '!', '?', ';', ':']
        strings_to_remove = [' - ', ' — ']
        for char in chars_to_remove:
            text = text.replace(char, '')
        for s in strings_to_remove:
            text = text.replace(s, ' ')
        return text

finder2 = WordsFinder('test_file.txt', "Walt Whitman - O Captain! My Captain!.txt", "Rudyard Kipling - If.txt", "Mother Goose - Monday’s Child.txt")
print(finder2.get_all_words()) # Все слова
print(finder2.find('for'))
print(finder2.count('for'))