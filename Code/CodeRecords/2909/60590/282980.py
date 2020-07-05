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

if arr == [] :
    print(0)
else:
    times = []
    for i in range(arr.__len__()):
        count = 0
        s1 = arr[i]
        for j in range(s.__len__() - s1.__len__() + 1):
            temp = s[j:j+s1.__len__()]
            if temp == s1:
                count += 1
        times.append(count)
    ans = max(times)
    print(ans)