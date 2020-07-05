num1=input()
num2=input()
res=0
for i in range(0,len(num1)):
    temp=num2+'0'*(len(num1)-1-i)
    res=int(temp)*int(num1[i])+res
print(res)