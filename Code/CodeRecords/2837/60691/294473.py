def getmax(l):
    length = l[0]
    limit = l[2]
    maxnum = 0

    for i in range(limit):
        maxnum += int(pow(2, i))
    for i in range(length-limit):
        maxnum += int(pow(2, limit-1))

    return maxnum


def getmin(l):
    length = l[0]
    limit = l[1]
    minnum = 0

    for i in range(limit):
        minnum += int(pow(2, i))
    for i in range(length-limit):
        minnum += 1

    return minnum


s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

result = ''
result += str(getmin(l))
result += ' '
result += str(getmax(l))

print(result)