from scipy.optimize import fsolve
import numpy as np
nums=int(input())
def func(i):
    x,y,z,m,n=i[0],i[1],i[2],i[3],i[4]
    return [
        x+y+z-p/4,
        x*y+y*z+x*z-s/2,
        y*z+m+n*(y+z),
        x*y+m+n*(x+y),
        x*z+m+n*(x+z)
    ]
for i in range(nums):
    [p, s] = list(map(int, input().split(" ")))
    r=fsolve(func,np.array([0.5,1.5,0.5,0,0]))
    print("{:.5f}".format(r[0]*r[1]*r[2]))