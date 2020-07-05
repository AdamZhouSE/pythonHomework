T = int(input())
for i in range(T):
    s = (''+input()).split(' ')
    s =  list(map(int,s))
    x = s[0]
    y = s[1]
    list1 = list(map(int,(''+input()).split(' ')))
    list2 = list(map(int,(''+input()).split(' ')))
    # print(list(set(list1).union(set(list2))))
    # list3 = (list(set(list1).union(set(list2))))
    # print(list3)
    list3 = list(map(int, (list(set(list1).union(set(list2))))))
    list3.sort()
    list3 = list(map(str,list3))
    # print(list3)
    for j in range(len(list3)):
        print(list3[j],end=' ')
    # print(list3[len(list3)-1])
    print()