num=int(input())
for nn in range(num):
    n=int(input())
    if n%5==0:
        print(-1)
    else:
        print(int(n%5))