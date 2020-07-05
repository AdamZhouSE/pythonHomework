
def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    root = line1[1]
    data = []
    for i in range(0,n):
        data.append(list(map(int,input().split(' '))))

    def findRoots(node,tree,r):
        roots_list = []
        i = 0
        tmp = tree.copy()
        while i < len(tmp):
            if r in roots_list:
                break
            if tmp[i][1] == node or tmp[i][2] == node:
                roots_list.append(tmp[i][0])
                node = tmp[i][0]
                del tmp[i]
                i = 0
            else:
                i += 1
        return roots_list

    m = int(input())
    res = []
    for i in range(0,m):
        line2 = list(map(int,input().split(' ')))
        u = line2[0]
        v = line2[1]
        u_roots = findRoots(u,data,root)
        if v in u_roots:
            res.append(v)
            continue
        j = 0
        while j < len(data):
            if data[j][2] == v or data[j][1] == v:
                if data[j][0] == u:
                    res.append(data[j][0])
                    break
                if data[j][0] in u_roots:
                    res.append(data[j][0])
                    break
                else:
                    v = data[j][0]
                    j = 0
            else:
                j += 1

    for i in range(0,len(res)):
        print(res[i])

solve()