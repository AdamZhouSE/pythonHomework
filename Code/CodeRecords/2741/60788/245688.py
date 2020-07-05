import sys
def f(li):
    if len(li)==1:
        return True
    for i in range(0,len(li)-1):
        if li[i]>=li[i+1]:
            return False
    return True

m=input()[1:]
m=m[0:len(m)-1]
s=[int(x) for x in m.split(',')]
for i in range(len(s),0,-1):
    for j in range(0,len(s)-i+1):
        if f(s[j:j+i]):
            print(i)
            sys.exit(0)
print(1)