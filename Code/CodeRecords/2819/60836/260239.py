import math
"""
学校有 n 个小组外出游玩，第 i 个小组有 si (1 ≤ si ≤ 4) 个人
同学们想要打出租，每辆车最多坐4个人
同个小组必须坐在同一辆车上，求最少需要多少辆车才能让同学们都坐上出租车
"""

n=int(input())
arr=[int(m) for m in str(input()).split(" ")]

num_1=arr.count(1)
num_2=arr.count(2)
num_3=arr.count(3)
num_4=arr.count(4)

result=num_4+min(num_1,num_3)+num_2//2
num_2=num_2%2
if num_1>num_3:
    num_1=num_1-num_3
    result=result+num_2+math.ceil((num_1-num_2*2)/4)
else:
    num_3=num_3-num_1
    result=result+num_2+num_3

print(result)