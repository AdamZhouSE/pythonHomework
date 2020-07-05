import sys
 
sys.setrecursionlimit(1000000)
def minParts(a,b,sum):
    if sum>100:
        return 99999
    if a==1:
        return sum+b-1
    elif b==1:
        return sum+a-1
    elif b==a or a==b:
        return 99999
    elif b>a:
        return minParts(a,b-a,sum+1)
    elif b<a:
        return minParts(a-b,b,sum+1)

n=int(input())
i=int(n//1.6)+1
min=9999
while i>=int(n//1.7)+1:
    temp=minParts(i,n,0)
    if(temp<min):
        min=temp
    i=i-1
print(min,end="")