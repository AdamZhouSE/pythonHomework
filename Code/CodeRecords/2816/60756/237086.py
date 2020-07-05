import math

firstLine=input()
n=int(firstLine)
secondLine=input().split()
secondLine.sort(key=int)
print(secondLine[math.ceil(n/2-1)])