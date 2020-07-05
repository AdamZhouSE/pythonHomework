def rotate(l):
    ltemp = [[]for i in range(len(l))]
    for i in range(len(l)):
        for j in range(len(l)):
            ltemp[i].append(0)

    for i in range(len(l)):
        for j in range(len(l)):
            ltemp[j][len(l)-i-1] = l[i][j]
    return ltemp


n = int(input())
nums = []
string = []
for i in range(n):
    nums.append(int(input()))
    string.append(input())

storage = []
for i in range(n):
    ltemp = list(map(int, string[i].split(' ')))
    larr = [[]for i in range(nums[i])]
    for x in range(nums[i]):
        for y in range(nums[i]):
            larr[x].append(ltemp[nums[i]*x+y])

    lresult = rotate(larr)
    str1 = ''
    for x in range(len(lresult)-1):
        for y in range(len(lresult)):
            str1 += str(lresult[x][y])
            str1 += ' '
    for y in range(len(lresult)-1):
        str1 += str(lresult[len(lresult)-1][y])
        str1 += ' '
    str1 += str(lresult[len(lresult)-1][len(lresult)-1])
    storage.append(str1)

for i in range(len(storage)):
    print(storage[i])




