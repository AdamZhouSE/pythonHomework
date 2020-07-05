src=input()
target=int(input())
d={"+":0,"-":1,"*":2,"#":3}
def compare(op1,op2):
    priority=[
        ">>><",
        ">>><",
        "<<><",
        ">>>="
    ]
    return priority[d[op1]][d[op2]]
def cal(num1,num2,op):
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    else:
        return num1*num2
def decode(src):
    if src.isalnum():
        if src[0]=="0" and len(src)>1:
            return -1
        return int(src)
    operand=[]
    operator=[]
    src+="#"
    i=0
    flag=True
    operator.append("#")
    while len(operator)!=0:
        if not src[i].isalnum():
            if compare(src[i],operator[-1])==">":
                num2=operand.pop()
                num1=operand.pop()
                operand.append(cal(num1,num2,operator.pop()))
            elif compare(src[i],operator[-1])=="<":
                operator.append(src[i])
                if i < len(src) - 1:
                    i += 1
            else:
                operator.pop()
        else:
            j=i
            while j<len(src) and src[j].isalnum():
                j+=1
            if src[i:j][0]=="0" and j-i>1:
                flag=False
                break
            operand.append(int(src[i:j]))
            i=j
    if flag==False:
        return -1
    return operand.pop()
size=len(src)
res=[]
operator=["+","-","*"]
def backtrack(src,res,start,idx):
    if decode(src)==target:
        res.append(src)
    for i in range(start,size):
        for op in operator:
            front=src[0:i+idx]
            back=src[i+idx:]
            src=front+op+back
            backtrack(src,res,i+1,idx+1)
            src=front+back

backtrack(src,res,1,0)
print(res)
