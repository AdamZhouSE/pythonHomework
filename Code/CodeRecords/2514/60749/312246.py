s1=input()
s2=input()
def findindex(c,s):
    for h in range(0,len(s)):
        if(s[h]==c):
            return h
    return -1
def issequence(s,t):
    index1=-1
    for h in s:
        t=t[index1+1:]
        index1=findindex(h,t)
        if(index1==-1):
            return False
    return True
print(issequence(s1,s2))