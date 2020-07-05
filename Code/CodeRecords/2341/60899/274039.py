numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int,input().split()))
    m = list0[0]
    n = list0[1]
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    list1.extend(list2)
    list1.sort()
    list3 = list(map(str, list1))
    str1 = ' '.join(list3)
    print(str1 + " ")