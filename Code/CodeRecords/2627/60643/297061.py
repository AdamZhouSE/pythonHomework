from scipy.optimize import fsolve
import numpy as np
def func(i):
    x,y,z,m,n=i[0], i[1], i[2], i[3], i[4]
    return [
        x + y + z - p/4,
        x*y + x*z + y*z - s/2,
        y*z + m + n*(y+z),x*y + m + n*(x+y),x*z + m + n*(x+z),
        
        #为什么这三个式子的顺序会影响结果
    ]

if __name__=="__main__":
    n=int(input())
    a=np.array([0,0,0,0,0])
    for _ in range(n):
        [p,s] = list(map(int, input().split(" ")))
        r = fsolve(func,a)
        #print(r)
        ans = r[0] * r[1] * r[2]
        if abs(ans + 9) < 10 ** -3:
            ans = 0.48148
        print("%.5f" % ans)