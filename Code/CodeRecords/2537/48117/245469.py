import heapq

numList = input()
numList = numList[1:-1].split(',')
k = int(input())

for index in range(len(numList)):
    numList[index] = int(numList[index])


print(heapq.nlargest(k, numList)[-1])