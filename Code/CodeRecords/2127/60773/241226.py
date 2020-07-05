num1=int(input())
s=input()
#print(s)
num2=""
list=s.split(",")
for i in list:
    num2=num2+i
num2=int(num2)
#print(num1)
#print(num2)
sum=1
for i in range(num2):
    sum=sum*num1
print(sum%1337)