def shuzu(a):
    a.sort()
    ans=0
    for x in a:
        if x==4:
            ans=ans+1
            a.pop()
    for x in a:
        if x==3 and a[0]==1:
            a.pop()
            a.pop(0)
            ans=ans+1
    if len(a)==0:
        return ans
    if a[0]==1:
        while len(a)>=2 and a[-1]==2 and a[1]==1:
            a.pop()
            a.pop(0)
            a.pop(0)
            ans=ans+1
        if len(a)==0:
            return ans
        if a[0]==1 and a[-1]==2:
            ans=ans+(len(a)-1)//2+1
        elif a[0]==1 and a[-1]==1:
            if len(a)%4==0:
                ans=ans+len(a)//4
            else:
                ans=ans+len(a)//4+1
        else:
            if len(a)%2==0:
                ans=ans+len(a)//2
            else :
                ans=ans+len(a)//2+1
    elif a[0]==2:
        while a[-1]==3:
            ans=ans+1
            a.pop()
        if len(a)%2==0:
                ans=ans+len(a)//2
        else :
            ans=ans+len(a)//2+1
    else:
        ans=ans+len(a)    
    return ans
num=input()
a=input()
a=a.split(' ')
a=[int(x) for x in a]
b=shuzu(a)
print(b)