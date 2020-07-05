t=int(input())
for ex in range(0,t):
    n=int(input())
    a=n
    s=""
    for i in range(0,n):
        s=s+"0"
    while n>9:
        s="9"+s
        n=n-9
    if not n==0:
        s=str(n)+s
    print(s)