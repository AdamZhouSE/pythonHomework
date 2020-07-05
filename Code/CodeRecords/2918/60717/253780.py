n=int(input())
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
count=0
while len(list1)!=0:
    minn=min(list1)
    list1.remove(minn)
    now=1
    while len(list1)!=0 and max(list1) >= now:
        minn=max(list1)
        for i in list1:
            if i >= now:
                minn=min(minn,i)
        list1.remove(minn)
        now+=1
    count+=1
print(count)