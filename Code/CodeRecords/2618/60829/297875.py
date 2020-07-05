n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    count=0
    for i in range(len(b)-1):
        if b[i]>b[i+1]:
            count=count+1
    print(count)