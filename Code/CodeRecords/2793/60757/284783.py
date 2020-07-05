l=input().split()
n=int(l[0])
c=int(l[1])
li=list(map(int,input().split()))
count=0
for i in range(n):
    if i==0:
        count=1
    else:
        if li[i]-li[i-1]<=c:
            count+=1
        else:
            if c==0:
                count=0
            else:
                count=1
print(count)
