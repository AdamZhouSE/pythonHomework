num=int(input())
for i in range(num):
    k=int(input())
    m=k
    nums=[]
    while(k>0):
        nums.append(k)
        k-=5
    while(k<=m):
        nums.append(k)
        k+=5
    for i in nums:
        print(i,end=" ")
    print()