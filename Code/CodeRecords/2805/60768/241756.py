n = int(input())
intList = input().split(' ')
intList = [int(x) for x in intList]
up = []
i = 1
for j in range(n - 1):
    if intList[j] < intList[j + 1]:
        i += 1
    else:
        up.append(i)
        i = 1
up.append(i)
up.sort()
longest = str(up[len(up) - 1])
print(longest)