length = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
tmp = [0 for i in range(100)]
tmp[4] = 0
tmp[8] = 1
tmp[15] = 2
tmp[16] = 3
tmp[23] = 4
tmp[42] = 5
res = []
for i in range(length):
    index = tmp[arr[i]]
    if index == 0:
        res.append([0])
    else:
        for j in range(len(res)):
            if len(res[j]) == index:
                res[j].append(0)
                break
            else:
                continue
count = 0
for i in res:
    if len(i) == 6:
        count += 6
print(length - count)
