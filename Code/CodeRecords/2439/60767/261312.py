class Node:
    def __init__(self, id, father=None, value=0):
        self.id = id
        self.father = father
        self.value = value


def create(arr):
    res = []
    flag = 0
    flag1 = 0
    for i in range(len(arr)):
        flag = 0
        if (arr[i][0] != 0):
            for y in res:
                flag1 = 0
                if (y.id == i):  # 看自己在不在res里
                    for x in res:
                        if (x.id == arr[i][0]):  # father已经在res里
                            y.father = x
                            flag1 = 1
                            y.value = arr[i][1]
                            break
                    if (flag1 == 0):
                        father = Node(arr[i][0])
                        y.father = father
                        y.value = arr[i][1]
                        res.append(father)
                    flag = 1
            if (flag == 0):  # 自己不在res里
                temp = Node(i)
                flag2=0
                for x in res:
                    if(x.id==arr[i][0]): #father在res里
                        temp.father = x
                        temp.value = arr[i][1]
                        res.append(temp)
                        flag2 = 1
                        break
                if(flag2==0):
                    father = Node(arr[i][0])
                    temp.value = arr[i][1]
                    temp.father = father
                    res.append(temp)
                    res.append(father)
    return res


def ans(arr, q):
    x = q[0]
    y = q[1]
    res = 0
    for node in arr:
        if (int(node.id) == int(y)):
            start = node
        if (int(node.id) == int(x)):
            end = node
    while (start.id != end.id):
        res ^= start.value
        start = start.father
    return res


n = int(input())
arr = [[0] * 2 for i in range(111)]
for i in range(n-1):
    temp = input().split()
    arr[int(temp[1])][0] = int(temp[0])
    arr[int(temp[1])][1] = int(temp[2])
res = create(arr)
k = int(input())
query = []
for i in range(k):
    temp = input().split()
    query.append([int(temp[0]), int(temp[1])])
for q in query:
    print(ans(res, q))
