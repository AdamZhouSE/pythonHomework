import math
def mcm(num):
    minimum = 1
    for i in num:
        minimum = int(i) * int(minimum) / math.gcd(int(i), int(minimum))
    return int(minimum)
number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
source.sort()
all=[]
for i in source:
    if(not i in all):
        all.append(i)
if(len(all)==1):
    print("Yes")
else:
    a=mcm(all)
    times=[]
    for i in range(len(all)):
        times.append(a/all[i])
    result=[]
    for i in times:
        x=i
        while(x%2==0):
            x=x/2
        while(x%3==0):
            x=x/3
        result.append(x)
    result.sort()
    if(result[-1]==1):
        print("Yes")
    else:
        print("No")

    