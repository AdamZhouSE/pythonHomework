def leastCount(num):
    if num==0:return 0
    if num%2==0: return leastCount(int(num/2))+1
    else: return leastCount(num-1)+1

res=[]
t=int(input())
for i in range(t):
    n=int(input())
    res.append(leastCount(n))
for e in res:print(e)
