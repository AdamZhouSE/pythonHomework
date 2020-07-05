a=long(input())
import math
def findK(n,s):
    return math.ceil(pow(n,1.0/s))-1

def sum(p,s):
    return (pow(p,s+1)-1)/(p-1)
small=1;large=70
for i in range(small,large):
    s=i
    k=findK(a,s)
    if(k>1 and a==sum(k,s)):
        print(k)
        break






