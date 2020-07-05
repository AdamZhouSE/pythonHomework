s=input()
ind=0
stack=[]
re=''
while(ind!=len(s)):
    if s[ind]=='[':
        stack.append('[')
        ind+=1
        if ord(s[ind+1])>=ord('0') and ord(s[ind+1])<=ord('9'):
            stack.append(s[ind:ind+2])
            ind+=1
        else:
            stack.append(s[ind])
        ind+=1
        tmp=''
        while s[ind]!=']' and s[ind]!='[':
            tmp+=s[ind]
            ind+=1
        if tmp!='':
            stack.append(tmp)
    elif s[ind]==']':
        str=stack.pop()
        d=int(stack.pop())
        stack.pop()
        tmp=''
        for i in range(d):
            tmp+=str
        if len(stack)>0:
            t=stack[len(stack)-1]
            if ord(t[0])>=ord('0') and ord(t[0])<=ord('9'):
                stack.append(tmp)
            else:
                stack[len(stack)-1]=t+tmp
        else:
            re+=tmp
        ind+=1
    else:
        re+=s[ind]
        ind+=1
print(re,end='')            
        