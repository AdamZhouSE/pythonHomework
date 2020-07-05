numOftests = int(input())
for i in range(numOftests):
    n = int(input())
    sum0 = 0
    for k in range(1,n+1):
        sum0+=(k+1)*k//2
    print(sum0)