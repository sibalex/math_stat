from typing import Callable, Any, Dict, List, Union

# for i in range(10):
#     if i%2 != 0:
#         continue
#     print(i)


def factorial(i: Union[int, float]) -> int:
    """
    3! = 1*2*3=6
    """
    if i is None:
        return None
    i = int(i)
    if i < 0:
        return None
    if i == 0:
        return 1
    return i * factorial(i-1)


def map_int_list(fnc: Callable, l: List[int]) -> List[int]:
    return [fnc(e) for e in l]


def map_int_dict(fnc: Callable, d: Dict[Any, int]) -> Dict[Any, int]:
    return {key: fnc(value) for key, value in d.items()}


print(factorial(3))
print(map_int_list(factorial, [0,1,2,3,4]))
print(map_int_dict(factorial, {'zero': 0, 'three': 3}))
print(factorial(3.01))
print(factorial(None))
