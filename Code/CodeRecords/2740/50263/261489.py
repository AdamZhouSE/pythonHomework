from dateutil.parser import parse
import math
Min = 1000000000
minus = 0
list = eval(input())
lost = []
for i in range(len(list)):
    list[i] = '2020-2-29/' + list[i] + ':00'
for i in range(len(list)):
    for j in range(len(list)):
        if i != j:
            minus = abs((parse(list[i])-parse(list[j])).seconds)
            Min = int(min(Min,minus/60))
print(Min)