n,t = map(int,input().split())
a=[int(n) for n in input().split()]
num=0
time=0
for i in range(0,n):
    if time+a[i]<=t:
        num=num+1
        time=time+a[i]
        continue
    else:
        break
print(num)
        