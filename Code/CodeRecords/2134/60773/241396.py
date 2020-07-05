import math
b=int(input())
die=int(input())
time=int(input())
state=time//die+1
print(math.ceil(math.log(b)/math.log(state)))
