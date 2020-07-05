n=int(input())
for i in range(n):
    k=int(input())
    tem=list(input().split(" "))
    for j in range(k-1):
        if int(tem[j])>int(tem[j+1]):
            print(tem[j+1],end=" ")
        else:
            print("-1",end=" ")
    if i==n-1:
        print("-1",end=" ")
    else:
        print("-1",end=" ")
        print("")