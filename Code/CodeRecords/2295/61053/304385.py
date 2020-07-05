if __name__ == "__main__":
    n,root = map(int,input().split(" "))
    dict = {}
    for i in range(n):
        f,l,r = map(int,input().split(" "))
        if l != 0:
            dict[l] = f
        if r != 0:
            dict[r] = f
    #print(dict)
    a,b = map(int,input().split(" "))

    lst1 = []
    lst2 = []
    while dict[a] != root:
        lst1.append(a)
        a = dict[a]
    lst1.append(a)
    lst1.append(root)
    while dict[b] != root:
        lst2.append(b)
        b = dict[b]
    lst2.append(b)
    lst2.append(root)

    #print(lst1)
    #print(lst2)

    lst1 = lst1[::-1]
    lst2 = lst2[::-1]
    index = 0
    while index < min(len(lst1), len(lst2)):
        if lst1[index] != lst2[index]:
            break
        index+=1
    print(lst1[index-1])