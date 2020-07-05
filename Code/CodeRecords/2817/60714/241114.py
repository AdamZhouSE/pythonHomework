n = int(input())
kids = [int(x) - 1 for x in input().split()]
length = 0
ans = False
for i in range(0, n):
    temp = i
    flags = [False for x in range(0, n)]
    while flags[temp] is False:
        flags[temp] = True
        temp = kids[temp]
        length += 1
    if temp is not i:
        length = 0
    if length is 3:
        ans = True
        print("YES")
        break
if ans is False:
    print("NO")
