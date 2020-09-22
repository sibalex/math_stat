from functools import wraps

def mapper(func):

  @wraps(func)
  def inner(list_of_values):
    """Test"""

    return [func(value) for value in list_of_values]
  return inner

@mapper
def camelcase(s):
  """Turn string_like_this into StringLikeThis"""

  return ''.join([i.capitalize() for i in s.split('_')])


name = ['T_test', 'Some_test']


print(camelcase(name))
print(camelcase.__doc__)
print()


##
import random

def power_of(exp):
  def decorator(func):
    def inner():
      return func() ** exponent
    return inner
  
  if callable(exp):
    exponent = 2
    return decorator(exp)
  else:
    exponent = exp
    return decorator
  # return decorator

@power_of
def rdd():
  return random.choice([1,2,3,4,5,6,7])

t = rdd()
print(t, round(t**(1/3)))

