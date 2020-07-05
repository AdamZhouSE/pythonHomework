s1=input()
s2=input()
def issequence(s,t):
    index1=-1
    for h in s:
        index1=t[index1+1:].index(h)
        if(index1==-1):
            return False
    return True
print(issequence(s1,s2))