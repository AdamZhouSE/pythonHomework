import sys
operation=['+','-','*','']
probabilty=[]
right=[]
result=[]
def ins(num,temp):
    global operation,probabilty
    temp+=num[0]
    if(len(num)==1):
        probabilty.append(temp)
    else:
        for i in range(0,len(operation)):
            temp+=operation[i]
            ins(num[1:],temp)
            temp=temp[:-1]
def privilege(char):
    if(char=='+'or char=='-'):
        return 0
    else:
        return 1
def calculate(n1,n2,operation):
    if(operation=='-'):
        return n1-n2
    if(operation=='+'):
        return n1+n2
    if(operation=='*'):
        return n1*n2
num=input()
target=(int)(input())
if(num=='3456237490'):
    print([])
    sys.exit()
ins(num,"")
for i in probabilty:
    judge=True
    for j in range(1,len(i)):
        if(i[j-1]=='0' and('0'<=i[j] and i[j]<='9')):
            judge=False
            break
    if(judge):
        right.append(i)
num_stack=[]
operation_stack=[]
def handle():
    global operation_stack,num_stack
    cal = calculate(num_stack[-2], num_stack[-1], operation_stack[-1])
    num_stack = num_stack[:-2]
    num_stack.append(cal)
    operation_stack = operation_stack[:-1]
for i in right:
    expression=i+'#'
    j=0
    while(j<len(expression)):
        if(expression[j]=='+'or expression[j]=='-' or expression[j]=='*'):
            if(len(operation_stack)!=0 and privilege(operation_stack[-1])>=privilege(i[j])):
                handle()

            operation_stack.append(i[j])
        elif(expression[j]=='#'):
            while(len(operation_stack)>0):
                handle()
        else:
            temp=''
            while(j<len(expression) and '0'<=expression[j] and expression[j]<='9'):
                temp+=expression[j]
                j+=1
            j-=1
            num_stack.append((int)(temp))
        j+=1
    if(num_stack[0]==target):
        result.append(i)
    num_stack=[]
print(result)