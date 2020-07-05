firstLine=input()
n=int(firstLine)
cost=0
ai=0
pi=101
for i in range(n):
    nextLine=input().split()
    ai=int(nextLine[0])
    if pi>int(nextLine[1]):
        pi=int(nextLine[1])
    cost+=(ai*pi)
print(cost)