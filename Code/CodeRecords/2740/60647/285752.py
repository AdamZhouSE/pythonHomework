list=input()
def minus(str1,str2):
    num11=int(str1[0])*10+int(str1[1])
    num12 = int(str1[3]) * 10 + int(str1[4])
    num1=num11*60+num12
    num21 = int(str2[0]) * 10 + int(str2[1])
    num22 = int(str2[3]) * 10 + int(str2[4])
    num2 = num21 * 60 + num22
    if num1>=num2:
        a=num1-num2
        b=num2+60*24-num1
        if a>=b:
            return b
        else:
            return a
    else:
        a = num2 - num1
        b = num1 + 60 * 24 - num2
        if a >= b:
            return b
        else:
            return a
res=24*60
for i in range(len(list)-1):
    for j in range(i+1,len(list)):
        temp=minus(list[i],list[j])
        if temp<=res:
            res=temp
print(res)