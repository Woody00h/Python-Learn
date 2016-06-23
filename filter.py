#filter

def is_odd(x):
    return bool(x%2)

def is_even(x):
    return not(x%2)
    
print is_even(5)
print is_even(6)
print is_odd(5)
print is_odd(6)

L = [0,1,2,3,4,5,6,7,8,9]

print filter(is_even, L)
print filter(is_odd, L)

def is_palindrome(n):
    s = str(n)
    head = 0
    tail = len(s) - 1
    while not(head == tail):
        if not(s[head]==s[tail]):
            return False
        head = head + 1
        tail = tail - 1
        if tail == 0:
            break
    return True

print is_palindrome(11)
print is_palindrome(12)
print is_palindrome(121)
print is_palindrome(123)
print is_palindrome(12321)

Ls = list(range(10,100))
print filter(is_palindrome, Ls)