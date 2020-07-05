n=int(input())
for i in range(n):
    t=int(input())
    if t%5==0:
        print(-1)
    else:
        print(str(t%5))