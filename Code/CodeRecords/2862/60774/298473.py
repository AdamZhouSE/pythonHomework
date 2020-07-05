def classify(numLst):
    odd = []
    even = []
    for num in numLst:
        if(num % 2 == 0):
            even.append(num)
        else:
            odd.append(num)
    odd.sort(reverse = True)
    even.sort(reverse = True)
    return [odd,even]

n = int(input())
numLst = list(map(int,input().split(' ')))
newLst = classify(numLst)
if(len(newLst[0]) > len(newLst[1]) + 1):
    newLst[0] = newLst[0][len(newLst[1]) + 1:]
    print(sum(newLst[0]))
elif(len(newLst[1]) > len(newLst[0]) + 1):
    newLst[1] = newLst[1][len(newLst[0]) + 1:]
    print(sum(newLst[1]))
else:
    print(0)