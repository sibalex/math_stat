a = 1
b = a
print(b)
a = 2
print(b)

a = []
b = a
a.append('test')
print(b)

def f():
    x = 1
try:
    print(x)
except Exception as e:
    print(e)

# замыкания
def one():
    x = ['one','two']
    ''' Внимание на X это объект вне тела inner
    замыкание это функция в теле которой есть ссылки на переменные
    которые были объявленны внутри ее тела в окружающем 
    ее области видимости (enclousen)
    при этом X не параметр inner, при таких условиях
    возможны замыкания
    '''
    def inner():
        print(x)
        print(id(x))
    return inner
o = one() # <= f(inner)
print(o)
o()
print(dir(o))
print(o.__closure__)
print(dir(o.__closure__[0]))
print(o.__closure__[0].cell_contents)

a = o.__closure__[0].cell_contents
print(id(a)) # a-140354548912064 == o-140354548912064

print(a)
o()
a.append('three')
o()