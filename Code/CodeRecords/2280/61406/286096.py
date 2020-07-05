T = int(input())
for a in range(0,T):
    N = int(input())
    source = input().split(' ')
    sum = N*(1+N)//2
    for i in source:
        sum = sum-int(i)
    print(sum)