import os

# - Napisz skrypt zliczający ilość plików w katalogu /dev (lub w dowolnym katalogu), skorzystaj ze standardowej biblioteki - os
# - Napisz rekurencyjne przejście drzewa katalogów i wypisanie plików, które znajdują się w podanym jako parametr katalogu


def listing_func(path='/dev', prefix=""):   # zmienna prefix wykorzystywana do wcięć przy wypisywaniu zawartości katalogów
    count = 0
    for entry in os.scandir(path):
        if entry.is_file():
            count = count + 1
            print(prefix, entry.name)
        elif entry.is_dir():
            print(prefix, entry.name)
            count = count + listing_func(entry.path, prefix+"\t")
    return count


if __name__ == "__main__":

    dir_path = r"C:\Users\Lukaszzieba\Desktop\pyton\Zadania1\dev"
    print("Number of files: ", listing_func(dir_path))
