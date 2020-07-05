T = int(input())
for a in range(0,T):
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        sum = sum+i*i
    print(sum)