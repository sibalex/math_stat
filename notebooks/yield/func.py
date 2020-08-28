def countdown(n):
    result = []
    while n != 0:
        result.append(n - 1)
        n -= 1
    return result

print(countdown(4))
# print(countdown(4))
