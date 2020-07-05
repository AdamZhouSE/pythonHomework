n,x=map(int,input().split())
c=[int(i) for i in input().split()]
c=sorted(c)
time=0
for num in c:
    if x>=1:
        time=time+num*x
    else:
        time=time+num
    x=x-1
print(time)