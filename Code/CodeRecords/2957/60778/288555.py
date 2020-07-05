def isStrange(s):
    a=s[0]
    b=s[len(s)-1]
    p=s.index(b)
    for i in range(p):
        if(s[i]!=a):
            return False
    for i in range(p,len(s)):
        if(s[i]!=b):
            return False
    return True

s=input()
count=0
has_count=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        if(isStrange(s[i:j+1])):
            if(not s[i:j+1] in has_count):
                has_count.append(s[i:j+1])
print(len(has_count))