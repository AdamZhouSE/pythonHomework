firstLine=input()
n=int(firstLine)
secondLine=input().split()
secondLine.sort(key=int)
if abs(int(secondLine[0])-int(secondLine[1]))>abs(int(secondLine[n-1])-int(secondLine[n-2])):
    print(abs(int(secondLine[n-1])-int(secondLine[1])))
else:
    print(abs(int(secondLine[n-2])-int(secondLine[0])))