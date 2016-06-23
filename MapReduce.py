#map/reduce
from functools import reduce

def square(x):
    return x*x
    
def add(x,y):
    return x+y
    
def char2int(x):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]
    
def intcombine(x,y):
    return 10*x + y
    
L = [0,1,2,3,4,5,6,7,8,9]
LS = '123456789'
print map(square,L)

print map(str,L)

print reduce(add, L)
print char2int('7')
print intcombine(1,2) + 3
print reduce(intcombine, map(char2int,LS))