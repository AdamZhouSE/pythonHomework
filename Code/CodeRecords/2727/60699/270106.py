n=int(input())
for j in range(n):
    input()
    list1 = list(map(int, input().split(' ')))
    list2 = list(map(int, input().split(' ')))
    list1.sort()
    list2.sort()
    res = 0
    for i in range(len(list2)):
        res = max(res, abs(list2[i] - list1[i]))
    print(res)