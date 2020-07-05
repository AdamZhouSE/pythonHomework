import math
def get(n,m):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        min=100
        for i in range(n,0,-1):
            sum=0
            sum=sum+1
            sum=sum+get(n-i*i,i)
            if sum<min:
                min=sum
        return min

num=int(input())
n = int(math.sqrt(num))
print(get(num,n))
