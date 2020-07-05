import math
num=input()
num=int(num)
cons=0
for i in range(2,num//2):
    if num/i==i:
        cons=1
        break
if cons==0:
    print("False")
else:print("True")