numOftests = int(input())
for i in range(numOftests):
    list2 = list(map(int, input().split()))
    length = list2[0]
    list0 = list(map(int,input().split()))
    list1 = list(map(int, input().split()))
    list0.sort()
    list1.sort()
    lengthOfzero = len(list0)
    list0.extend(list1)
    list0 = list(set(list0))
    if len(list0) == lengthOfzero:
        print("Yes")
    else:
        print("No")