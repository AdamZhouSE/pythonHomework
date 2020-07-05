tmp = input()
tmp = [int(x) for x in tmp.split(" ")]
n = tmp[0]
m = tmp[1]
tmp = input()
arr = [int(x) for x in tmp.split(" ")]
count1 = 0
count2 = 0

for i in range(n):
    if arr[i] == -1:
        count1 += 1
    else:
        count2 += 1
minCount = min(count1,count2)
for i in range(m):
    tmp = input()
    tmp = [int(x) for x in tmp.split(" ")]
    l = tmp[0]
    r = tmp[1]
    width = r - l + 1

    if width % 2 == 1:
        print(0)
        continue
    else:
        if width // 2 <= minCount:
            print(1)
        else:
            print(0)
