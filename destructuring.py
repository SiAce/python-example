def f(a, b, c, d, *args, **kwargs):
    print(args)
    print(kwargs)

def g(a, b, c, d):
    print(a, b, c, d)


f(1, 2, 3, 4, 5, 6, e=5, f=6)

a, b, c, d, *args = (1, 2, 3, 4, 5, 6)

d = {"b": 2, "c": 3, "d": 4}
a = 1

g(a, **d)
