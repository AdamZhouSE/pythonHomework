import math
num=int(input())
ra=int(str(math.sqrt(num)).split(".")[0])
a=1
for i in range(1,ra+1):
    for j in range(1,ra+1):
        if j*j+i*i==num:
            a=0
            break
if a==0:
    print(True)
else:
    print(False)