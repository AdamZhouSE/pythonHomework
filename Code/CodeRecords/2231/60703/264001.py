T = int(input())
import  math
res = []
iin = []
for m in range(T):

    N = int(input())
    if(N==1):
        res.append(0)
        continue
    iin.append(N)
    sqr = int(math.sqrt(N))+1
    for j in range(2,sqr+2):
        if N%(j*j) ==0:
            res.append(0)
            break
        if(j == sqr+1):
            res.append(1)

for i in res:
    print(i)