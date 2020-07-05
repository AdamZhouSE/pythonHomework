num1=int(input())
num2=int(input())
num11=num1
num22=num2
if num1<0:
    num11=-num1
if num2<0:
    num22=-num2
count=0
while num11>0:
    num11=num11-num22
    count+=1
count=count-1
if num1*num2<0:
    count=-count
print(count)