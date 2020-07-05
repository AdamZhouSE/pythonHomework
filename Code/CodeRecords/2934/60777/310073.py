s=input()

def unpack(s):
    x=-1
    y=-1
    for i in range(len(s)):
        if(s[i]=='['):
            x=i
            break
    for j in range(len(s)-1,-1,-1):
        if(s[j]==']'):
            y=j
            break
    if(x!=-1):
        stack=[]
        for i in range(len(s)):
            if(s[i]=='['):
                stack.append(i)
            elif(s[i]==']'):
                get=stack.pop()
                if(get==x):
                    y=i
                
    if(x==-1):
        res=''
        i=0
        num=''
        pre=''
        c=0
        while(i<len(s)):
            if(s[i].isdigit()):
                pre=''
                j=i
                while(j<len(s) and s[j].isdigit()):
                    num+=s[j]
                    j+=1
                i=j
                c=int(num)
            else:
                j=i
                while(j<len(s) and not s[j].isdigit()):
                    pre+=s[j]
                    j+=1
                i=j
                if(c==0):
                    c=1
                res+=pre*c
        return res
    else:
        num=''
        ind=0
        for i in range(x):
            if(s[i].isdigit()):
                num+=s[i]
            else:
                ind=i
                break
        if(num!=''):
            num=int(num)
        if(s[:x].isdigit()):
            res=(unpack(s[x+1:y])+unpack(s[y+1:]))*int(s[:x])
        else:
            if(num==''):
                num=1
            res=(unpack(s[ind:x])+unpack(s[x+1:y])+unpack(s[y+1:]))*num
        return res

res=unpack(s)
print(res,end='')
                
                    
                
                
    
        