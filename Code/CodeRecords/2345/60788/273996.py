def f(s):
    if len(s)==1:
        return 0
    s.sort()
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            return s[i]
    return 0
def g(s):
    if len(s)==1:
        return 0
    for i in range(0,len(s)-1):
        if s[i]!=i+1:
            return i+1
    return 0
num=int(input().strip())
for i in range(num):
    length=int(input().strip())
    s=[int(x) for x in input().strip().split()]
    print(str(f(s))+' '+str(g(s)))