import math
list1 = []
hang = 0
lie = 0
for i in range(5):
    listtemp = input().split(" ")
    listtemp = [int(listtemp[j]) for j in range(5)]
    list1.append(listtemp)
    for k in range(5):
        if listtemp[k]==1:
            hang=i
            lie=k
result = math.fabs(hang-2)+math.fabs(lie-2)
print(result)