numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    list1 = []
    list2 = []
    for x in list0:
        if x%2==1:
            list1.append(str(x))
        else:
            list2.append(str(x))
    list2.extend(list1)
    str0 = ' '.join(list2)
    str0+=" "
    print(str0)