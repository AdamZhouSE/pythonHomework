import re
num1=re.split('\+|i',input())
num2=re.split('\+|i',input())
a_real=int(num1[0])
a_img=int(num1[1])
b_real=int(num2[0])
b_img=int(num2[1])
real=a_real*b_real-a_img*b_img
img=a_real*b_img+b_real*a_img
print(str(real)+'+'+str(img)+'i')