a=input()
b=input()
num1=0
num2=0
index1=1
index2=1
for item in a:
    if item=='1':
        num1=num1+index1
    index1=index1*2
for item in b:
    if item=='1':
        num2=num2+index2
    index2=index2*2
num=num1+num2
result=''
while num>0:
    num=num//2
    if num%2==1:
        result='1'+result
    else:
        result='0'+result
print(result)