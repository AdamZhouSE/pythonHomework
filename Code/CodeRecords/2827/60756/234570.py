firstLine=input()
n=int(firstLine)
secondLine=input().split()
secondLine.sort(key=int)
print(' '.join(secondLine))