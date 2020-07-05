n=int(input())
li=list(map(int,input().split()))
li=sorted(li)
sign=0
for i in range(len(li)-2):
    if li[i]+li[i+1]>li[i+2]:
        sign=1
        break
if sign==0:
    print('NO')
else:
    print('YES')