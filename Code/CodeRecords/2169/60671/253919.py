time=int(input())
while(time>0):
    time-=1
    string=input()
    stack=[]
    for c in string:
        if('0'<=c<='9'):
            stack.append(int(c))
        else:
            num2=stack.pop()
            num1=stack.pop()
            if(c=='+'):
                stack.append(num1+num2)
            elif(c=='-'):
                stack.append(num1-num2)
            elif(c=='*'):
                stack.append(num1*num2)
            elif(c=='/'):
                stack.append(num1/num2)
    print(stack.pop())