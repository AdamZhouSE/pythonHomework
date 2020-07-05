nums=input()
n=[]
n=nums.split(",")
n=[int(x) for x in n]
lower=int(input())
upper=int(input())
total=0

if lower>upper:
    total=-1
else:
    for i in range(len(n)):
        if n[i]>=lower and n[i]<=upper:
            total=total+1#单独一个满足条件
    for i in range(0,len(n)):
        j=i+1
        he=n[i]
        while j<=len(n)-1:
            he=he+n[j]
            if he>=lower and he<=upper:
                total=total+1
                break
            j=j+1

print(total)