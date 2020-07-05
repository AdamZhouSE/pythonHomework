t=int(input())
for i in range(t):
    n=int(input())
    flag=0
    for i in range(1,n):
        if i**3>n:
            break
        flag=i
    print(flag)