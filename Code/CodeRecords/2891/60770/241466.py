from functools import reduce
input()
pis=list(map(int,input().split()))
theMax=reduce(lambda x,y:max(x,y),pis)
res=reduce(lambda x,y:x+y,map(lambda x:theMax-x,pis))
print(res)