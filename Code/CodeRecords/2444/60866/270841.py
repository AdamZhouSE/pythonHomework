def paixu(a,k,t):
    while k>0:
        for i in range(0,len(a)-k):
            if a[i]-a[i+k]<=t and a[i]-a[i+k]>=-t:
                print('true')
                return
        k=k-1    
    print('false')
import re
a=input()
m=re.split(r'\s+',a)
b=eval(m[2].rstrip(','))
c=m[5].rstrip(',')
paixu(b,int(c),int(m[8]))