s = input()
maxletters = int(input())
minSize = int(input())
maxSize = int(input())

arr = []
for j in range(maxSize - minSize + 1):
    length = minSize + j
    for i in range(s.__len__() - length + 1):
        temp = s[i:i + length]
        #print(temp)
        sets = set(temp)
        #print(sets)
        if sets.__len__() <= maxletters:
            arr.append(temp)
            #print(arr)
#print(arr)

Maxtimes = s.count(arr[0])
for i in range(1, arr.__len__()):
    times = s.count(arr[i])
    if times > Maxtimes:
        Maxtimes = times
print(Maxtimes)