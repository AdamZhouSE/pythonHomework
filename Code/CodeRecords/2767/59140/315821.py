t = int(input())
res=[]
for _ in range(t):
    n=int(input())
    res.append(n)
    while n%5!=0:
        n-=3
        if n<0:break
    if n<0:print(0)
    else:
        nums=n//5
        result=1
        result+=nums//2
        result += nums // 3
        print(result)