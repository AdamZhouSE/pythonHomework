import math
n, time = int(input()), int(1/int(input()) * int(input()))
pig = math.log(n, time+1)
pig = math.ceil(pig)
print(pig)