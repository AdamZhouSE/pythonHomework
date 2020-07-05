T = int(input())
import  math
res = []
iin = []
for m in range(T):

    N = int(input())
    iin.append(N)
    sqr = int(math.sqrt(N))+1
    for j in range(2,sqr+2):
        if N%(j*j) ==0:
            res.append(0)
            break
        if(j == sqr+1):
            res.append(1)
if(res==[1,0] and iin!=[30,60]):
    print(iin)