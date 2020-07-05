import math
n=int(input())
num=n
result=""
maxN=int(math.floor(math.log(num+1)/math.log(2)))-1
for n in range(maxN,1,-1):
    q=int(max(math.floor(math.pow(num,1/n)),2))
    s=(pow(q,n+1)-1)/(q-1)
    if abs(num-s)<0.001:
        result=str(q)
if result==str(q):
    print(result)
else:
    print(str(num-1))