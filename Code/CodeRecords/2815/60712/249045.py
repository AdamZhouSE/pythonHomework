n = int(input())
list1 = list(map(int,input().split()))
numNegative = 0
minPositive = 0
hasZero = False
result = 0
for i in range(n):
    if list1[i]==0:
        hasZero =True
    if list1[i]<0:
        result = result+(-1-list1[i])
        numNegative +=1
    else:
        result = result+abs(list1[i]-1)
if numNegative%2!=0:
    if hasZero:
        print(result)
    else:
        print(result+2)
else:
    print(result)

