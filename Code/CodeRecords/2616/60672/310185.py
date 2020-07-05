def nums(string):
    num1=''
    num2=''
    index=0
    for i in range(len(string)):
        if string[i]!=' ':
            num1+=string[i]
        else:
            index=i
    for i in range(index+1,len(string)):
        if string[i]!='':
            num2+=string[i]
    return float(num1),float(num2)


t=int(input())
for i in range(t):
    n=input()
    num1,num2=nums(n)
    if (num1-num2*(num2-1.0)/2.0)/num2>=1:
        print(1)
    else:
        print(0)