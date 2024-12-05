# 6. Napisać obiektowo prosty dekorator na funkcji wypisującej jakiś string,
# a celem dekoratora jest zamiana liter w napisie na duże litery

class UppercaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, str):
        return self.func(str.upper())


def some_func(str):
    print(str)


if __name__ == "__main__":
    some_func("try1")
    new_func = UppercaseDecorator(some_func)
    new_func("try2")
