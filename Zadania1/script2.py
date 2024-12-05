import re

# - Napisz skrypt usuwający z wejściowego ciągu tekstowego (można plik wygenerowa
#  samemu lub ściągnąć np. z portalu informacyjnego) wybrane słowa podane jako parametr wejściowy


def deleting_func(text, words):
    clean_text = text
    for word in words:
        pattern = re.compile(word)
        clean_text = re.sub(pattern,"",clean_text)
    return clean_text


if __name__ == "__main__":
    words = ['Owca', 'Kot']     # słowa do usunięcia
    text = "Kot Pies Owca Osa"  # tekst

    print(text)
    print(deleting_func(text, words))