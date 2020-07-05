import re

data2D = []
for i in range(5):
    userInput = input()
    info = re.split('\s', userInput)
    data = []
    try:
        for number in info:
            data += [int(number)]
        data2D += [data]
    except:
        break
for i in range(5):
    for j in range(5):
        if(data2D[i][j]==1):
            r=i
            c=j

print(abs(i-3)+abs(j-3))