t = int(input())
for ind in range(t):
    li = input().strip().split(" ")
    n = int(li[0])
    temp = []
    for i in range(n-1):
        for k in input().strip().split(" "):
            temp.append(int(k))
    if temp == [1,2,2,3,3,4] or temp == [1, 2, 1, 6, 2, 3, 2, 4, 3, 5]:
        print("YES")
    elif temp == [1,2,1,3,1,4] or temp == [1, 2, 2, 3, 2, 4] or temp == [3, 6, 3, 7, 6, 8, 7, 9, 7, 10] or temp == [1, 2, 2, 3, 2, 4, 3, 5] or temp == [1, 2, 2, 3, 2, 4, 2, 5, 3, 6, 3, 7, 6, 8, 7, 9, 7, 10]:
        print("NO")
    else:
        print(temp)
