firstLine=input().split()
secondLine=input().split()
n=int(firstLine[0])
x=int(firstLine[1])
secondLine.sort(key=int)
time=0
for i in range(n):
    time+=int(secondLine[i])*x
    if x!=1:
        x-=1
print(time)