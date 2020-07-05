
def func(s:str):
    stack=[]
    number=[]
    length=len(stack)
    s='('+s+')'
    for i in s:
        if ['+','-','(',')'].count(i)>0 :
            if i!=')':

                stack.append(i)
                length=len(stack)
            else:
                while stack[-1]!='(':
                    if stack[-2]=='-':
                        if stack[-1]=='-':
                            stack[-1]='+'
                        if stack[-1]=='+':
                            stack[-1]='-'
                    temp=0
                    if stack[-1]=='+':
                        temp=number[-1]+number[-2]
                    if stack[-1]=='-':
                        temp=number[-2]-number[-1]
                    del stack[len(stack)-1]
                    del number[len(number)-1]
                    del number[len(number)-1]
                    number.append(temp)
                del stack[len(stack) - 1]

        else:
            if i!=' ':
                number.append(int(i))
    return number[0]
print(func(input()))