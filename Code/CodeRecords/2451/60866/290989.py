def chazhao(a,b):
    for i in range(0,len(a)):
        if a[i]==b:
            return i
        elif a[i]>b:
            j=i
            return j
    return len(a)
import re
a=input()
b=re.split(r'[\s\[\]\,]+',a)
c=[int(x) for x in b[1:-1]]
print(chazhao(c,int(b[-1])))