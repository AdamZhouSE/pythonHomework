n=int(input())
for i in range(n):
    k=int(input())
    key=0
    num=list(input().split(" "))
    for j in range(k):
        num[j]=int(num[j])
    for j in range(k-1):
        key=0
        for m in range(j+1,k):
            if num[j]<num[m]:
                key=1
                continue
        if key==0:
            print(num[j],end=" ")
    print(num[-1])