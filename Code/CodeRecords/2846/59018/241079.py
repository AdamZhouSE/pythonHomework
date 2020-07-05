n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
b=set(a)

if 0 in b:
    print(len(b)-1)
else:
    print(len(b))

        