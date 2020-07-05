def f(s):
    if s[0]+s[1]==s[2]:
        return True
    elif s[0]+s[2]==s[1]:
        return True
    elif s[1]+s[2]==s[0]:
        return True
    else:
        return False
def g(s):
    if len(s)<=2:
        return -1
    else:
        count=0
        for i in range(len(s)-2):
            for j in range(i+1,len(s)-1):
                for k in range(j+1,len(s)):
                    if f([s[i],s[j],s[k]]):
                        count+=1
                        
        if count>0:
            return count
        else:
            return -1

a=int(input().strip())
for i in range(a):
    length=int(input().strip())
    s=[int(x) for x in input().strip().split()]
    print(g(s))
