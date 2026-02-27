def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


a = 3
b = 7
for value in squares(a, b):
    print(value)