s=input()
t=input()
for j in range(len(t),len(s)+1):
    for i in range(len(s)-j+1):
        a=s[i:i+j]
        res=1
        for k in t:
            if k not in a:
                res=0
                break
        if(res==1):
            print(a)
            break
    if(res==1):
        break
if(res==0):
    print("")