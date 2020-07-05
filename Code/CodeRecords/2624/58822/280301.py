def com(a):
    if(len(a)==1):
        return [int(a)]
    res=[]
    num=0
    for i in range(len(a)):
        ch=a[i]
        if(ch=='+' or ch== '-' or ch=='*'):
            left=com(a[0:i])
            right=com(a[i+1:len(a)])
            if(ch=='+'):
                for i in range(0,len(left)):
                    for k in range(0,len(right)):
                        num=left[i]+right[k]
                        res.append(num)
            else:
                if(ch=='-'):
                    for i in range(0, len(left)):
                        for k in range(0, len(right)):
                            num = left[i] - right[k]
                            res.append(num)
                else:
                    for i in range(0, len(left)):
                        for k in range(0, len(right)):
                            num = left[i] * right[k]
                            res.append(num)
    return res

res=[]
n=input()
b=eval(n)
res.extend(com(n))
print(res)