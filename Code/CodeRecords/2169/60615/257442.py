
time=int(input())
result=[]
opset=['+','-','*','/']
while time>0:
    postfix=[i for i in input()]    #231*+9-
    num=[]

    for item in postfix:
        if item not in opset:
            num.append(int(item))
        else:
            if item=='+':
                temp=num[-2]+num[-1]
            elif item=='-':
                temp=num[-2]-num[-1]
            elif item=='*':
                temp=num[-2]*num[-1]
            else:
                temp=num[-2]/num[-1]
            del num[-2:]
            num.append(temp)
    result.append(num[0])
    time=time-1
for res in result:
    print(res)

