numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int,input().split()))
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))
    list1.extend(list2)
    list1.sort()
    print(list1[list0[2]-1])