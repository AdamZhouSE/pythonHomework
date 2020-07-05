def calR(num1,num2):
    if (num1=='0')|(num2=='0'):
        return '0'
    n1=len(num1)
    n2=len(num2)
    res=[0 for i in range(n1+n2)]
    for i in range(n1-1,-1,-1):
        temp1=int(num1[i])
        for j in range(n2-1,-1,-1):
            temp2=int(num2[j])
            temp=res[i+j+1]+temp1*temp2
            res[i+j+1]=temp%10
            res[i+j]+=temp//10
    res=[str(i) for i in res]
    result= ''.join(res)
    while result[0]=='0':
        result=result[1:]
    return result


num1=input()
num2=input()
print(calR(num1,num2))