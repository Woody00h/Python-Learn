#map/reduce
from functools import reduce

def square(x):
    return x*x
    
def add(x,y):
    return x+y
    
def dig(x):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]
    
def strcombine(x,y):
    return 10*dig(x) + dig(y)
    
L = [0,1,2,3,4,5,6,7,8,9]
LS = ['0','1','2','3','4','5','6','7','8']
print map(square,L)

print map(str,L)

print reduce(add, L)
print dig('7')
print strcombine('1','2')
print reduce(strcombine, LS)