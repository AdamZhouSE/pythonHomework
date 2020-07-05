n=int(input())
list1=[]
for i in range(0,n):
    list1.append(int(input()))
summ=list1[0]
for i in range(1,n):
    minn=list1[i]
    for j in range(0,i):
        minn=min(minn,abs(list1[i]-list1[j]))
    summ+=minn
print(summ,end='')