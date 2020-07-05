s=list(input())
n=[0,0,0,0]
temp=""
for i in range(0,len(s)):
    if s[i]=="x" or (s[i]=="-" and temp=="") or (s[i]>="0" and s[i]<="9"):
        temp+=s[i]
    elif s[i]=="-" and not temp=="":
        if temp[-1]=="x":
            temp=temp[0:len(temp)-1]
            if temp=="":
                temp="1"
            elif temp=="-":
                temp="-1"
            n[0]+=int(temp)
        else:
            n[1]+=int(temp)
        temp="-"
    elif s[i]=="+":
        if temp[-1]=="x":
            temp=temp[0:len(temp)-1]
            if temp=="":
                temp="1"
            elif temp=="-":
                temp="-1"
            n[0]+=int(temp)
        else:
            n[1]+=int(temp)
        temp=""
    elif s[i]=="=":
        if temp[-1]=="x":
            temp=temp[0:len(temp)-1]
            if temp=="":
                temp="1"
            elif temp=="-":
                temp="-1"
            n[0]+=int(temp)
        else:
            n[1]+=int(temp)
        temp=""
        k=i
        break
for i in range(k+1,len(s)):
    if s[i]=="x" or (s[i]=="-" and temp=="") or (s[i]>="0" and s[i]<="9"):
        temp+=s[i]
    elif s[i]=="-" and not temp=="":
        if temp[-1]=="x":
            temp=temp[0:len(temp)-1]
            if temp=="":
                temp="1"
            elif temp=="-":
                temp="-1"
            n[2]+=int(temp)
        else:
            n[3]+=int(temp)
        temp="-"
    elif s[i]=="+":
        if temp[-1]=="x":
            temp=temp[0:len(temp)-1]
            if temp=="":
                temp="1"
            elif temp=="-":
                temp="-1"
            n[2]+=int(temp)
        else:
            n[3]+=int(temp)
        temp=""
    elif s[i]=="=":
        if temp[-1]=="x":
            temp=temp[0:len(temp)-1]
            if temp=="":
                temp="1"
            elif temp=="-":
                temp="-1"
            n[2]+=int(temp)
        else:
            n[3]+=int(temp)
        temp=""
if not temp=="":
    if temp[-1]=="x":
        temp=temp[0:len(temp)-1]
        if temp=="":
            temp="1"
        elif temp=="-":
            temp="-1"
        n[2]+=int(temp)
    else:
        n[3]+=int(temp)
a=n[0]-n[2]
b=n[3]-n[1]
if a==0:
    if b==0:
        print("Infinite solutions")
    else:
        print("No solution")
else:
    print("x="+str(b//a))