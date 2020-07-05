def func2():
    temp = list(map(int, input().strip().split(" ")))
    n = temp[0]
    root = temp[1]
    tree = []
    while n > 0:
        n -= 1
        tree.append(list(map(int, input().strip().split(" "))))
    ans = [[root]]
    def check(a:list):
        for i in range(len(a)):
            for j in range(len(tree)):
                if tree[j][0] == a[i]:
                    if tree[j][1] != 0 or tree[j][2] != 0:
                        return True
                    else:
                        break
        return False
    cur = 0
    while True:
        if not check(ans[cur]):
            break
        temp = []
        for i in range(len(ans[cur])):
            for j in range(len(tree)):
                if tree[j][0] == ans[cur][i]:
                    if tree[j][1] != 0:
                        temp.append(tree[j][1])
                    if tree[j][2] != 0:
                        temp.append(tree[j][2])
                    break

        ans.append(temp)
        cur += 1
    for i in range(len(ans)):
        print("Level %d : "%(i+1),end="")
        for j in range(len(ans[i]) - 1):
            print(ans[i][j], end=" ")
        print(ans[i][len(ans[i]) - 1])
    for i in range(len(ans)):
        if i % 2 == 0:
            print("Level %d from left to right: "%(i+1),end="")
            for j in range(len(ans[i]) - 1):
                print(ans[i][j], end=" ")
            print(ans[i][len(ans[i]) - 1])
        else:
            print("Level %d from right to left: "%(i+1),end="")
            for j in range(len(ans[i])-1,0,-1):
                print(ans[i][j], end=" ")
            print(ans[i][0])
    return
func2()