numOftests = int(input())
for i in range(numOftests):
    list2 = list(map(int, input().split()))
    length = list2[0]
    list0 = list(map(int,input().split()))
    list1 = list(map(int, input().split()))
    list0.sort()
    list1.sort()
    result = True
    for j in range(len(list1)):
        if list1.count(list1[j]) > list0.count(list1[j]):
            result = False
    if result:
        print("Yes")
    else:
        print("No")