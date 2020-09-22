import time

# def calc_square(numb):
#   start = time.time()
#   res = []
#   for i in numb:
#     res.append(i**2)
#   end = time.time()
#   print(f'calc square took {str((end-start)*1000)} mil sec')
#   return res

def time_it(func):
  def wrapper(numb):
    start = time.time()
    result = func(numb)
    end = time.time()
    print(f'{func.__name__} took {str((end-start)*1000)} mil sec')
    return result
  return wrapper

@time_it
def calc_square(numb):
  return [i**2 for i in numb]

b = calc_square(range(1000))
# print(b)