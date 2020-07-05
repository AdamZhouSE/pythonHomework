n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
maxx=1
for i in range(0,n-1):
    count=1
    j=i+1
    tmp=list1[i]
    nextt=list1[j]
    while j<=n-1:
        if nextt<2*tmp:
            count+=1
            tmp=nextt
            j+=1
            if j!=n:
                nextt=list1[j]
        else:
            break
    maxx=max(maxx,count)
print(maxx)