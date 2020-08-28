from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

# @timeit
def one(n):
    # start = datetime.now()
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    # print(datetime.now() - start) # 0:00:00.000041
    return l

# @timeit
def two(n):
    # start = datetime.now()
    l = [i for i in range(n) if i % 2 == 0]
    # print(datetime.now() - start) # 0:00:00.000022
    return l

l1 = one(10**2) # без @timeit ~ timeit(one()) c @timeit one()
l2 = two(10**2)

# print(l1) 
# print(l2)

ll = timeit(one) # <= тоже самое если включить @timeit
ll1 = timeit(one)(10) # => wrapper(10) => one(10)

# print(ll)
print(ll1)



