n=int(input())
a=input().split(' ')
a=list(set(a))
a.sort()
b=len(a)
if b<3 or (b==3 and int(a[1])-int(a[0])==int(a[2])-int(a[1])):
    print('YES')
else:
    print('NO')
