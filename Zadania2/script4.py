# 4. Zaimplementuj własny iterator o nazwie fibonacci, zwracający kolejne liczby ciągu Fibonacciego. Funkcja __init__ powinna posiadać parametr o nazwie steps określający liczbę wyrazów ciągu, po których funkcja  __next__  rzuca wyjątek StopIteration


class Fib:
    def __init__(self, steps):
        self.steps = steps
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.steps:
            raise StopIteration
        self.count += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a


if __name__ == "__main__":
    n = 7
    fib = Fib(n)

    for i in fib:
        print(i)