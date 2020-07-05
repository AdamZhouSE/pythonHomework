import math
num = int(input())
max=0
for splits in range(2,num+1):
    add1=num%splits
    rs=pow(int(num/splits),splits-add1)*pow(int(num/splits)+1,add1)
    if rs>max:max=rs
print(max)
