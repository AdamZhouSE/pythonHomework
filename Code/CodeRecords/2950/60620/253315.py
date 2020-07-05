s=input()
num=0
answer=0
x=0
if(len(s)%2==1):
    x=-1
else:
    for i in range(len(s)):
        if(s[i]=='2'):num+=1
        if(s[i]=='5'):num-=1
        if(num<0):
            x=-1
            break
        answer=max(num,answer)
if(x==-1):print(x)
else:print(answer)


