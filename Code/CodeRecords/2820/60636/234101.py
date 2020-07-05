import numpy as np 
number=int(input(""))
time=[]
result=[]
for i in range(number):
    a=input("")
    min=a.split(" ")
    b=int(min[0])*60+int(min[1])
    time.append(b)
for i in range(number):
    a=time.count(time[i])
    result.append(a)
print(max(result))