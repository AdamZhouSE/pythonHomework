nums = int(input())
res = []
for i in range(nums):
    list1 = []
    n = int(input())
    list2 = input().split(" ")
    list2 = [int(i) for i in list2]
    k = int(input())
    for m in range(len(list2) - 1):
        for j in range(m + 1, len(list2)):
            if list2[m] + list2[j] == k:
                list1.append([list2[m], list2[j], k])
    res.append(list1)
for i in res:
    if not i:
        print(-1)
    else:
        for j in i:
            j = [str(a) for a in j]
            print(" ".join(j))