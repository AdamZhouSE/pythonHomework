n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
a.sort()
b=[str(y) for y in a]
print(' '.join(b))
