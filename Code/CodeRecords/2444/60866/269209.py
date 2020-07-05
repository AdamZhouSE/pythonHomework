def paixu(a,k,t):
    for i in range(0,len(a)-t):
        if a[i]-a[i+t]==k or a[i]-a[i+t]==-k:
            print('true')
            return
    print('false')
import re
a=input()
m=re.split(r'\s+',a)
b=eval(m[2].rstrip(','))
c=m[5].rstrip(',')
paixu(b,int(c),int(m[8]))