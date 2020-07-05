t=int(input())
for i in range(t):
    n=int(input())
    sum=3
    if n>1:
        for i in range(n-1):
            sum+=7+i*4
    print(sum)