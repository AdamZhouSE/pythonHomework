def isSub(s,t):
    if len(s)>len(t):
        return False
    start=0
    num=0
    for i in range(len(s)):
        contrast=s[i]
        for j in range(start,len(t)):
            if t[j]==s[i]:
                start=j+1
                num+=1
                break
        if num==len(s):
            return True
    return False

s=input()
t=input()
print(isSub(s,t))