count=int(input())
for i in range(count):
    info=input().split()
    n=int(info[0])
    k=int(info[1])
    rear=[i for i in range(n)]
    index=0
    while len(rear)!=1:
        for j in range(k-1):
            index=(index+1)%len(rear)
        del rear[index]
    print(rear[0]+1)