def cal(n):
    if n==2:
        return 3
    elif n==1:
        return 2
    else:
        return cal(n-1)+cal(n-2)

n=int(input())
for i in range(0,n):
    num=int(input())
    print(cal(num))