def so(s,t):
    s=str(s)
    temp=s
    for i in t:
        if i not in s:
            return ""
    res="A"*100000
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            count=0
            temp=s[i:j+1]
            for k in t:
                if k  in temp:
                    count+=1
            if count==len(t):
                if len(temp)<len(res):
                    res=temp
    return res
s=input()
t=input()
print(so(s,t))