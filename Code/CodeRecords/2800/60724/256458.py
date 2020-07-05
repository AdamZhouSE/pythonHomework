fir=input().split()
d=int(fir[1])
num=input().split()
num=[int(x) for x in num]
times=0
for i in range(1,len(num)):
    while num[i-1]>=num[i]:
        times=times+1
        num[i]=num[i]+d
print(times)