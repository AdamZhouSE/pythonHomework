t=int(input())
for nn in range(t):
    n=int(input())
    b=list(eval(input().replace(' ',',')))
    k=int(input())
    mul=1
    for i in b:
        mul = (mul * (i % k)) % k
    print(mul%k)
