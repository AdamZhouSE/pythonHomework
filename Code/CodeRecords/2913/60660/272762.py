import functools
t=int(input())
l = eval('[' + input().replace(' ', ',') + ']')
def add(a,b):
    return a+b
if functools.reduce(add,l)%2==0:
    print('YES')
else:
    print('NO')
