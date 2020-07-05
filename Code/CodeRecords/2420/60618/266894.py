n=int(input())
for i in range(1,n):
    re=[i,n-i]
    a=list(str(i))
    b=list(str(n-i))
    if ('0' not in a) and ('0' not in b):
        print(re)