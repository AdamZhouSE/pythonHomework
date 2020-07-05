n = int(input())
l = [[] for i in range(n)]
for i in range(n):
    length = int(input())
    temp = list(map(int, input().split()))
    temp.sort()
    l[i] = (temp)
# print(l)
for i in range(n):
    temp = [[0] * 2 for j in range(len(l[i]))]
    pre = l[i][0]
    num = 0
    m = 0
    for k in range(len(l[i])):
        if l[i][k] != pre:
            temp[m][0] = num
            temp[m][1] = pre
            num = 1
            pre = l[i][k]
            m += 1
        else:
            num += 1
        if k == len(l[i]) - 1:
            temp[m][0] = num
            temp[m][1] = pre
  #  print(temp)
    temp.sort(key=lambda s: (-s[0], s[1]))
    s = ""
    for p in range(len(temp)):
        for q in range(temp[p][0]):
            s = s + str(temp[p][1]) + " "
    print(s, end="")
    print()

