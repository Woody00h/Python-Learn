#generator

L = [x*x for x in range(1,10)]
print L

g = (x*x for x in range(1,10))

for x in g:
    print x
    
# print next(g)
# print next(g)
# print next(g)
# print next(g)
# print next(g)
# print next(g)
# print next(g)

def fibonacci(max=10):
    a = 0
    b = 1
    n = 0
    while(n<max):
        yield n
        n = a + b
        b = a
        a = n
    # return "Done"

for x in fibonacci(20):
    print x
