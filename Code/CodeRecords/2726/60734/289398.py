import math
lst = input().split(',')
lst[0]= lst[0][1:]
lst[-1] = lst[-1][:-1]
index = lst.index('null')
print(math.floor(math.log(index+1,2)))