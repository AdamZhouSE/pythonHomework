n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
b=[]
a.sort()
for i in range(n):
    if len(a)>1:
        a.pop(-1)
        a.pop(0)
    else:
        break

for j in a:
    b.append(str(j))
print(' '.join(b))