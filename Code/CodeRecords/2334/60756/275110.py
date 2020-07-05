from itertools import combinations
def isTrangle(point:tuple):
    x,y,z=point
    return x+y>z and x+z>y and y+z>x

arr=list(map(int,input().split(",")))
ans=filter(isTrangle,combinations(arr,3))
try:    
    print(sum(max(ans,key=sum)))
except:
    print(0)