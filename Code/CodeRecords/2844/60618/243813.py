n,t = map(int,input().split())
a=[int(n) for n in input().split()]
number=0
num=0
time=0
for i in range(0,n):
    for j in range(i,n):
        if time+a[j]<=t:
            num=num+1
            time=time+a[j]
            continue
        else:
            if num>number:
                number=num
            time=0
            num=0
            break
    
print(number)
        