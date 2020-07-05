def judge(n):
    if n<2:return False
    else:
        for i in range(2,n):
            if n%i==0:return False
        return True

t = int(input())
for _ in range(t):
    n=int(input())
    if judge(n+2):print("Yes")
    else:print("No")
