n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
a.sort()
b=map(lambda x:str(x),a)
print(' '.join(b))
