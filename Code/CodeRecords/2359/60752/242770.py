num=int(input())
for i in range(num):
    size=int(input())
    a=list(map(int,input().split(' ')))
    a.sort()
    count=0
    for m in range(size-2):
        ele1=a[m]
        for n in range(m+1,size-1):
            ele2=a[n]
            for k in range(n+1,size):
                ele3=a[k]
                if ele1+ele2==ele3:
                    count+=1
    if count==0:
        count=-1
    print(count)

