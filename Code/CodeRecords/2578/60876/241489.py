import sys
import math
list=sys.stdin.readline().split(",")
target=int(input())
result=1
while True:
    sum=0
    for item in list:
        sum+=(math.ceil(int(item)/result))
    if sum<=target:
        print(result)
        break
    else:
        result+=1