def gen_func(x):
    for i in range(x):
        yield i

test = gen_func(7)

for i in test:
    print(i)