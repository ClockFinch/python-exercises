# 1.  Stwórz klasę implementującą liczby zespolone oraz przeciąż dla niej operatory dodawania i odejmowania


class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self,other):
        return ComplexNum(self.re+other.re, self.im+other.im)

    def __sub__(self,other):
        return ComplexNum(self.re-other.re, self.im-other.im)

    def __str__(self):
        if self.im <=0:
            return f"{self.re} - {-self.im}i"
        else:
            return f"{self.re} + {self.im}i"


if __name__ == "__main__":
    a = ComplexNum(1,3)
    b = ComplexNum(5,-4)
    c = a + b
    d = a - b
    print(c)
    print(d)