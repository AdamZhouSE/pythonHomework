a=input()

  

res=0
i=0
while i<len(a):
    if a[i]=='M':
        res+=1000
    elif a[i]=='D':
        res+=500
    elif a[i]=='C':
        if a[i+1]=='M':
            res+=900
            i+=1
        elif a[i+1]=='D':
            res+=400
            i+=1
        else:
            res+=100

    elif a[i]=='L':
        res+=50
    elif a[i]=='X':
        if a[i+1]=='C':
            res+=90
            i+=1
        elif a[i+1]=='L':
            res+=40
            i+=1
        else:
            res+=10
    elif a[i]=='V':
        res+=5
    elif a[i]=='I':
        if i==len(a)-1:
            res+=1
            break
        if a[i+1]=='X':
            res+=9
            i+=1
        elif a[i+1]=='V':
            res+=4
            i+=1
        else:
            res+=1
    i+=1
print(res)