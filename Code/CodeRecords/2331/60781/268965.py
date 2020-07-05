import re

str1=input()
n=int(str1[0])
m=int(str1[2])
k=int(str1[4])
data2D = []
for i in range(n):
    userInput = input()
    info = re.split('\s', userInput)
    data = []
    try:
        for number in info:
            data += [int(number)]
        data2D += [data]
    except:
        break;
Min=[]
for i in range(n):
    Min.append(min(data2D[i]))
Min.sort()
print(Min[n-k])
