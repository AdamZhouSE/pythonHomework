import math
num1=input()
num2=input().split(' ')
num2=[int(x) for x in num2]
if(num2[0]==0):
    print("UP")
elif(len(num2)==1):
    print("-1")
elif(num2[-1]==0):
    print("UP")
elif(num2[-1]>num2[-2])and num2[-1]!=15:
    print("UP")
elif(num2[-1]<num2[-2])and num2[-1]!=0:
    print("DOWN")
elif(num2[-1]==15):
    print("DOWN")
else:
    print("-1")