def eval(sign,num2,num1):
    num1=int(num1)
    num2=int(num2)
    if sign=='+':return num1+num2
    if sign=='-':return num1-num2
    if sign=='*':return num1*num2
    if sign=='/':return num1/num2

for b in range(int(input())):

    s=list(input())
    num=[]
    for ss in s:
        if ss.isnumeric():
            num.append(ss)
        else:num.append(eval(ss,num.pop(),num.pop()))

    print(num.pop())




