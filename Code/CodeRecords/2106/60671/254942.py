string=input()
string=string.replace(" ","")
stack=[]
operand=0
res=0
sign=1
for c in string:
    if ('0'<=c)and(c<='9'):
        operand=(operand*10)+int(c)
    elif(c=='+'):
        res+=sign*operand
        sign=1
        operand=0
    elif(c=='-'):
        res+=sign*operand
        sign=-1
        operand=0
    elif(c=='('):
        stack.append(res)
        stack.append(sign)
        sign=1
        res=0
    elif(c==')'):
        res+=sign*operand
        res*=stack.pop()
        res+=stack.pop()
        operand=0
print(res+sign*operand)
