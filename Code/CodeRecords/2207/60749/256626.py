def judge(n,k):
    sum=0
    for i in range(1,k+1):
        sum+=i
    if n>=k:
        return True
    else:
        return False
n=int(input())
res=[]
for _ in range(n):
    res.append(input().split(" "))
for h in res:
    if judge(int(h[0]), int(h[1])):
        print("1",end="\n")
    else:
        print("0",end="\n")