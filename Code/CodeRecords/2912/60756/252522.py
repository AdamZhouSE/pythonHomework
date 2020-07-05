s=list(input())
if len(s)<=1:
    print(len(s))
else:
    ans=1
    x=0
    y=1
    while y<=len(s):
        if (y-x)==len(set(s[x:y])):
            y+=1
        else:
            x+=1
            if y-x>ans:
                ans=y-x
    print(ans)