All = input().split(' ')
n = int(All[0])
k = int(All[1])

names = []

for i in range(0, n):
    get = input().split(' ')
    if int(get[1]) == 0:
        names.append(get[0])
    else:
        names.append(get[0] + names[int(get[1]) - 1])

for q in range(0, k):
    ans = 0
    get = input()
    length = len(get)
    for i in range(0, n):
        if length>len(names[i]):
            continue
        isInterested = True
        for j in range(0, length):
            if get[j] != names[i][j]:
                isInterested = False
                break
        if isInterested:
            ans += 1
    print(ans)
