t=int(input())
for nn in range(t):
    a=int(input())
    b=a-3
    if b%3==0:
        print(b,b+1,b+2)
    else:
        print(-1)