s=list(map(int,input().split(',')))
def isT(x,y,z):
    if(x+y>z):
        return True
    return False
s=sorted(s)
t=[]
for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        for k in range(j+1,len(s)):
            if(isT(s[i],s[j],s[k])):
                t.append([s[i],s[j],s[k]])
if(t==[]):
    print(0)
else:
    print(sum(t[-1]))