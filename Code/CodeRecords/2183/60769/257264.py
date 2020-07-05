num = int(input())
for j in range(num):
    n = int(input())
    sum = 0
    for i in range(n*(n-1)+1,n*(n+1)+1):
        sum += i
    print(sum)