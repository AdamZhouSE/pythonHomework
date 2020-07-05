def compute(s):
    ans=[]
    if s.isdigit():
        ans.append(int(s))
        return ans
    for i in range(len(s)):
        if not s[i].isdigit():
            op1s=compute(s[:i])
            op2s=compute(s[i+1:])
            for op1 in op1s:
                for op2 in op2s:
                    if(s[i]=='+'):
                        ans.append(op1+op2)
                    elif(s[i]=='-'):
                        ans.append(op1-op2)
                    else:
                        ans.append(op1*op2)
    return ans
                    
s=input()
print(compute(s))
