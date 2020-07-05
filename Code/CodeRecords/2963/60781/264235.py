import re
n=int(input())
data2D = []
i=0
while i<n-1 :
    i+=1
    userInput = input()
    info = re.split('\s+',userInput)
    data = []
    try:
        for number in info:
            data+=[int(number)]
        data2D+=[data]
    except:
        break;
print(data2D)