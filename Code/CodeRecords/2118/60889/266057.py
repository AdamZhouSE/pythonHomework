import math

num = int(input())
if num==0:
    print(False)
elif math.log(num,3)==int(math.log(num,3)):
    print(True)
else:
    print(False)