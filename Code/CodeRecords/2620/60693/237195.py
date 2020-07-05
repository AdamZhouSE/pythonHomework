cases=int(input())
for x in range(cases):
    n=int(input())
    sum=0
    for i in range(n+1):
        sum+=pow(i,5)
    print(sum)