import math

num=input()   #5
input=input()    #1 2 4 3 3

list=input.split(" ")

result=0
for item in list:
    result+=int(item)

result=math.ceil(result/4)       # 直接加起来 除4 向上取整
# 但 3人组数量比1人组数量 每多出来4个 会出现一次错误 车的数量需要加1 不足4个不会出错

one=list.count("1")
three=list.count("3")
add=0
if three>=one+4:
    diff=three-one
    add=math.floor(diff/4)

print(result+add)
