import math
lists = list(map(int, input().split(",")))
average = int(sum(lists))/ lists.__len__()
average = math.ceil(average)
times = 0
for i in range(lists.__len__()):
    times+=abs((average-int(lists[i])))
print(times)