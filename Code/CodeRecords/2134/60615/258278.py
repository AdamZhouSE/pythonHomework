import math
barral=int(input())
timeToDie=int(input())
time=int(input())
num=math.ceil(math.log(barral,(time//timeToDie)+1))
print(num)