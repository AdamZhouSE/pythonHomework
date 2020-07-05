t =int(input())
for i in range(t):
    n = int(input())
    sum = 0
    li = [int(x) for x in input().split()]
    for j in range(n):
        for k in range(j,n):
            if li[j]>li[k]:
                sum+=1
    print(sum)