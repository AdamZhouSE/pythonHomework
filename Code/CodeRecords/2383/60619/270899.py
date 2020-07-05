t = int(input())
for ind in range(t):
    li = input().split(" ")
    n = int(li[0])
    k = int(li[1])
    tree = []
    for p in range(n-1):
        list1 = input().split(" ")
        if int(list1[0])-1 < len(tree):
            tree[int(list1[0])-1].append(int(list1[1])-1)
        else:
            tree.append([int(list1[1])-1])
    if n != k**2:
        print("NO")
    else:
        result = True
        for j in tree:
            if len(j) > k:
                result = False
                break
        if result:
            print("YES")
        else:
            print("No")