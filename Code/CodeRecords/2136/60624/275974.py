import math
def func23():
    n = int(input())
    n_max = int(math.floor(math.log(n+1)/math.log(2)))-1
    flag = True
    for i in range(n_max,1,-1):
        j = int(max(math.floor(math.pow(n,1/i)),2))
        k = (pow(j,i+1)-1)/(j-1)
        if abs(n-k) < 0.001:
            flag = False
            print(j)
            break
    if flag:
        print(n-1)
    return
func23()