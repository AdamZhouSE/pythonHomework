firstLine=input()
n=int(firstLine)
secondLine=input().split()
thirdLine=input().split()
a=int(thirdLine[0])
b=int(thirdLine[1])
years=0
for i in range(a-1,b-1):
    years+=int(secondLine[i])
print(years)