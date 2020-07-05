def ans(stairs):
    numOfstairs = 0
    res = []
    for i in range(1,len(stairs)):
        if(stairs[i]<=stairs[i-1]):
            numOfstairs += 1
            res.append(stairs[i-1])
    res.append(stairs[-1])
    return res

n = int(input())
temp = input().split(" ")
stairs = []
for t in temp:
    stairs.append(int(t))
res = ans(stairs)
print(len(res))
for i in range(len(res)-1):
    print(res[i],"",end="")
print(res[-1])

