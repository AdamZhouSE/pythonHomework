s=input()
t=input()
while(t in s):
    if(s==t):
        break
    re=0
    for i in range(0,len(s)-len(t)+1):
        if(s[i:i+len(t)]==t):
            re=i
            break
    s=s[0:i]+s[i+len(t):]
print(s,end="")
