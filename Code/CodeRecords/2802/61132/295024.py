import math
n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(enumerate(l),key=lambda x:(math.ceil(x[1]/m),x[0]),reverse=True)
print(l[0][0]+1)