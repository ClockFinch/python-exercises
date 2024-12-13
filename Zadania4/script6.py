x = [1,2,3,4]

test = list(map(lambda a : a**a, x))

is_even = lambda a : a%2==0
even_test = list(filter(is_even, x))

print(test)
print(even_test)