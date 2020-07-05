import math
n=int(input())
if (n/2)%1==0 and math.sqrt(n/2)%1==0:
    print('True')
    exit()
start=int(math.sqrt(n/2));end=start+1
while end**2 <=n and start>0:
    if start**2+end**2==n:
        print('True')
        exit()
    elif start**2+end**2<n:
        end+=1
    else:
        start-=1
print('False')