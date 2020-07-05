p=int(input())
for i in range(p):
    n=int(input())
    r=0
    for j in range(1,n+1):
        r+=j*j
    print(r)