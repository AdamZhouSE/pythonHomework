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
    if n % k != 0:
        print("NO")
    else:
        count = 0
        result = True
        for j in tree:
            if len(j) == k:
                count += 1
            elif len(j) > k:
                result = False
        if result:
            if count > 1:
                print("NO")
            else:
                print("YES")
        else:
            print("NO")