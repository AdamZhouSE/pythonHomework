import math
s = input()[8:]
i = 0
temp =""
while s[i]!="]":
    temp += s[i]
    i+=1
array = temp.split(",")
array = [int(x) for x in array]
line = s.split(", ")
k = int(line[1][-1])
t = int(line[2][-1])
sentinel = 0
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if math.fabs(array[i]-array[j])<=t and math.fabs(i-j)<=k:
            print("true")
            sentinel = 1
            break
    if sentinel == 1:
        break
if sentinel == 0:
    print("false")


