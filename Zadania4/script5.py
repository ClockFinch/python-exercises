
def func(a):
    return lambda b : a * b

g = func(5)
print(g(3))