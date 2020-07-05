import math
num1=input()
num2=input()
res=0
for i in range(len(num1)):
    for j in range(len(num2)):
        res=res+math.pow(10,i+j)*int(num1[len(num1)-1-i])*int(num2[len(num2)-1-j])
print(int(res))