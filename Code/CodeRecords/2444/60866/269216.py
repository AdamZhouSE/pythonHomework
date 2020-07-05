def paixu(a,k,t):
    for i in range(0,len(a)-k):
        if a[i]-a[i+k]==t or a[i]-a[i+k]==-t:
            print('true')
            return
    print('false')
import re
a=input()
m=re.split(r'\s+',a)
b=eval(m[2].rstrip(','))
c=m[5].rstrip(',')
paixu(b,int(c),int(m[8]))