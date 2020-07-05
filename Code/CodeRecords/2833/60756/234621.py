firstLine=input()
n=int(firstLine)
secondLine=input().split()
thirdLine=input().split()
ml=0
for i in secondLine:
    ml+=int(i)
thirdLine.sort(key=int)
capacity=int(thirdLine[n-1])+int(thirdLine[n-2])
if(capacity>=ml):
    print("YES")
else:
    print("NO")