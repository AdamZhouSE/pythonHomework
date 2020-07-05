num=int(input())
temp=bin(num)[2:]
res=''
for i in temp:
    if i=='0':
        res +='1'
    else:
        res +='0'
num1=int(res,2)
print(num1)