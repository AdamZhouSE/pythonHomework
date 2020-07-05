list1 = input().split(",")
list1 = [int(i) for i in list1]
k = int(input())
res = False
for i in range(len(list1) - 1):
    for j in range(1, len(list1) - i):
        if sum(list1[i:j + 1]) % k == 0:
            res = True
            break
    if res:
        break
print(res)
