n=int(input())
res=[]
def number(n,k):
    return k-n-1
for _ in range(n):
    res.append(input().split(" "))
for h in res:
    print(number(int(h[0]),int(h[1])))