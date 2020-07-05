T = int(input())
import  cmath
for m in range(T):
    N = int(input())
    sqr = int(cmath.sqrt(N))+1
    for j in range(2,sqr+1):
        if N%(j*j) ==0:
            print(1)
            break
        if(j == sqr):
            print(0)