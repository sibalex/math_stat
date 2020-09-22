import time

def ins(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'start: {start} end: {end} total: {(end-start)*10000}')
        return result 
    return wrapper

@ins
def div(a,b):
    return a**b

t = div(5,5)
print(t)
