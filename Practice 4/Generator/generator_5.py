def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = 5
for number in countdown(n):
    print(number)