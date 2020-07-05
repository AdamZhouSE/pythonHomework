def addBit(a, b, c):
    s = int(a) + int(b) + c
    return str(s%2), int(s/2)

def add(a, b, l):
    c = 0
    result = ''
    for i in range(l):
        index = -1-i
        s, c = addBit(a[index], b[index], c)
        result = s + result
    return result.lstrip('0')

def fill(s, n):
    for i in range(n-len(s)):
        s = '0'+s
    return s

a = input()
b = input()
l = 1 + max(len(a), len(b))
a = fill(a, l)
b = fill(b, l)
result = add(a,b,l)
print(result)