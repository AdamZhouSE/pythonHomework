numList = eval(input())
for i in range(0,len(numList),2):
    if numList[i] != numList[i+1]:
        print(numList[i])
        break