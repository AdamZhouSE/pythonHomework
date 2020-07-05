s1=input()
s2=input()
def issequence(s,t):
    index1=-1
    for h in s:
        t=t[index1+1:]
        index1=t.index(h)
        if(index1==-1):
            return False
    return True
print(issequence(s1,s2))