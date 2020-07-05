import numpy as np
li = eval(input())
#print(li)
result=[]
for i in li:
    temp= i.split(':')
    temp1 = temp[0]+temp[1]
    temp2 = int(temp1)
    result.append(temp2)
#print(result)
result2 = np.sort(result)
#print(result2)
result1 = []
if(result2[0] == 0):
    result1.append(2360-result2[len(result2)-1])
result1.append(2360-result2[len(result2)-1]+result2[0])

#print(result1)
tm = 0
for i in range(len(result2)-1):
    result1.append(result2[i+1]-result2[i])
#print(result1)

_min =min(result1)
#print(_min)
yu = _min%100
h = int(_min /100)
if(_min <= 60):
    print(_min)
else:
    print(h*60+yu)


    