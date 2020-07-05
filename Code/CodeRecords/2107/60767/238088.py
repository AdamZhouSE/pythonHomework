import math
num = int(input())
if(math.log(num,2)-math.ceil(math.log(num,2))==0):
    print(True)
else:
    print(False)