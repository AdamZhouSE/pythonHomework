def judge(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    if sum<n*2:
        return 1
    return 0

t=int(input())
for i in range(t):
    number=int(input())
    print(judge(number))