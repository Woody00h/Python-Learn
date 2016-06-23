#high-order function

print abs(-100)

f = abs
print f(-100)

def MyAdd(x,y,f):
    return f(x)+f(y)
    
print MyAdd(-5,-6,abs)