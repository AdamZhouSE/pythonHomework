import math

def cal(x,y):
    return (x+y)/math.sqrt(2)

n=int(input())
ans=[]
for i in range(0,n):
    lis=list(map(int,input().split(" ")))
    ans.append(cal(lis[0],lis[1]))


print(round(max(ans)*math.sqrt(2)))