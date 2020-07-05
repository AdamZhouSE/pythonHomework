n=int(input())
res=[]
for _ in range(n):
    res.append(int(input()))
def Feb(n):
    if n==2:
        return 3
    elif n==3:
        return 5
    return Feb(n-1)+Feb(n-2)
for t in res:
    res=pow(2,t)-Feb(t)
    print(str(res))