n=int(input())
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
mini=0
min=a[0]
#print(a)
def rev(a,now,min):
    if now==min:
        return min+1
    else:
        tmp=a[now:min+1]
        tmp.reverse()
        for i in range(now,min+1):
            a[i]=tmp[i-now]
        #print(a)
        return min+1
res=[]    
for i in range(len(a)-1):
    for j in range(i,len(a)):
        if a[j]<min:
            min=a[j]
            mini=j
    res.append(rev(a,i,mini))
    #print(a)
    mini=i+1
    min=a[i+1]
res.append(len(a))
for i in res:
    print(i,end=' ')