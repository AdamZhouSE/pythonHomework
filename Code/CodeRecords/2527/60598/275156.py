import functools
line = input()[1:-1]
veg = int(input())
maxPrice = int(input())
maxDistance = int(input())
i = 0
L = len(line)
restaurants = []
temp = ""
while i < L:
    if line[i] == "[":
        i += 1
        temp = ""
        while i < L and line[i] != "]":
            temp += line[i]
            i += 1
        listR = list(map(int, temp.split(",")))
        if veg == 1 and listR[2] == 0:
            continue
        else:
            if listR[3] <= maxPrice and listR[4] <= maxDistance:
                restaurants.append(listR)
        i += 1
    else:
        i += 1


def com(list1, list2):
    if list1[1] > list2[1]:
        return -1
    elif list1[1] < list2[1]:
        return 1
    else:
        if list1[0] > list2[0]:
            return -1
        else:
            return 1


# print(restaurants)
# print(sorted(restaurants, key=functools.cmp_to_key(com)))
result = sorted(restaurants, key=functools.cmp_to_key(com))
ans = []
for i in result:
    ans.append(i[0])
print(ans)
