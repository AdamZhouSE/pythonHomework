n=int(input())
lis=list(map(int,input().split(' ')))
count=0
temp=lis[0]
a=[]
for i in lis:
    if(i!=temp):
        if(temp==0):
            a.append(count)
        else:
            a.append(-count)
        temp=i
        count=0
    count+=1
a.append(count)
#print(a)
c=0
count=0
for i in a:
    if(i<0):
        c+=1
    else:
        break
all=[]
temp=0
for i in range(c,len(a)-1):
    if(a[i]<0):
        if(a[i]+a[i+1]>=0):
            temp+=a[i]
        else:
            all.append(temp)
            temp=0
            continue
    else:
        temp+=a[i]
re=0
for i in range(0,c):
    re=re-a[i]
print(re+max(all))
    
    