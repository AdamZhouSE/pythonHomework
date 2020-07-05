def chazhao(a,b):
    if len(a)!=len(b):
        print('false')
    else:
        A=[ord(x) for x in a]
        B=[ord(x) for x in b]
        s1=set(A)
        s2=set(B)
        if len(s1|s2)!=len(s1):
            print('false')
        else:
            print('true')
import re
a=input()
m=re.split(r'\"',a)
a=m[1]
b=m[3]
chazhao(a,b)