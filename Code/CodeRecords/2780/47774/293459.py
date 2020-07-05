t=int(input())
for nn in range(t):
    n=int(input())
    b=list(eval(input().replace(' ',',')))
    k=int(input())
    sum=1
    for i in b:
        sum*=i
    print(i%k)
