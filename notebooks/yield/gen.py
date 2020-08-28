def get_countdown(n):
    while n != 0:
        yield n - 1 
        n -= 1

g = get_countdown(4)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for i in get_countdown(4):
    print(i)
