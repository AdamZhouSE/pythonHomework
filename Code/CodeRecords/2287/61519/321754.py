n=int(input())
for i in range(n):
    k=int(input())
    num=list(input().split(" "))
    for j in range(k-1):
        key=0
        for m in range(j+1,k):
            if num[j]<num[m]:
                print(num[m],end=" ")
                key=1
                break
        if key==0:
            print(-1,end=" ")
    print(-1)