def change(start,end,p1,p2,p3):
    res=""
    i=chr(ord(start)+1)
    while i<end:
        if p1==3:
            c='*'
        else:
            if i.isalpha():
                if p1 == 1:
                    c = i.lower()
                elif p1 == 2:
                    c = i.upper()
            else:
                c = i
        for j in range(p2):
            res=c+res if p3==2 else res+c
        i=chr(ord(i)+1)
    return res

p1,p2,p3=map(int,input().split())
s=input()
res=""
for i in range(len(s)):
    if i!=0 and s[i]=='-' and s[i+1]>s[i-1] and ((s[i+1].isalpha() and s[i-1].isalpha())or(s[i+1].isdigit() and s[i-1].isdigit())):
        res+=change(s[i-1],s[i+1],p1,p2,p3)
    else:
        res+=s[i]
print(res)
