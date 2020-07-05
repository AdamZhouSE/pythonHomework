import math
list=eval(input())
record={}

for item in list:
    if record.get(item)==None:
        record[item]=1
    else:
        record[item]=record.get(item)+1

result=[]
for item in record:
    if record.get(item) > math.floor(len(list)/3):
        result.append(item)

print(result)