t = int(input())
for ind in range(t):
    li = input().split(" ")
    n = int(li[0])
    k = int(li[1])
    tree = []
    nodes = []
    for p in range(n-1):
        list1 = input().split(" ")
        if int(list1[0]) in nodes:
            tree[nodes.index(int(list1[0]))].append(int(list1[1]))
        else:
            nodes.append(int(list1[0]))
            tree.append([int(list1[1])])
    if n != k**2:
        print("NO")
    else:
        result = True
        count = 0
        for j in tree[len(tree)-1]:
            if len(tree[nodes.index(j)]) > k-1:
                result = False
            elif len(tree[nodes.index(j)]) == k-1:
                count += 1
        if result:
            if len(tree[len(tree)-1]) - count + 1 == k:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")