def change(b,x):
    count=0
    for i in range(0,x-1):
        for j in range(i+1,x):
            if b[i]>b[j]:
                count=count+1
    return count
n=int(input())
for i in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    x=change(b,a)
    print(x)