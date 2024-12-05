import re

# - Napisz skrypt zmieniający w podanym ciągu wejściowym (można plik wygenerowa
#  samemu lub sciągnąć np. z portalu informacyjnego) wybrane słowa innymi slowami (podanymi w strukturze typu słownikowego) podanymi jako parametr wejściowy funkcji


def swapping_func(text, words):
    clean_text = text
    for word in words:
        pattern = re.compile(word)
        clean_text = re.sub(pattern, words[word], clean_text)
    return clean_text


if __name__ == "__main__":
    words = {
        'Pies': 'Bark',
        'Kot': 'Meow'
    }
    text = "Kot Pies Owca Kon"

    print(text)
    print(swapping_func(text, words))