n=int(input())
for i in range(n):
    m=int(input())
    list1=input().split()
    list1=[int(x) for x in list1]
    q=m
    while(q>0):
        sum=0
        for j in list1:
            if j>=q:
                sum+=1
        if sum>=q:
            print(q)
            break
        else:
            q-=1