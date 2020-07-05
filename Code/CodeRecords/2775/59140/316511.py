t = int(input())
for _ in range(t):
    n=int(input())
    if n%3!=0:print(-1)
    else:
        print(str(n//3-1)+" "+str(n//3)+" "+str(n//3+1))