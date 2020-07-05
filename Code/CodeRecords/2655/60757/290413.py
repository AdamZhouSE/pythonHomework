def judge(a):
    while(a!=1):
        if a%2==1:
            return False
        a=a//2
    return True
t=int(input())
for i in range(t):
    n=int(input())
    while(True):
        if judge(n):
            print(n)
            break
        else:
            n=n+1