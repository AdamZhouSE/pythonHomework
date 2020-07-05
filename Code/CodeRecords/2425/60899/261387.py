numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int, input().split()))
    length = list0[0]
    k = list0[1]
    list1 = list(map(int,input().split()))
    upper = 10000
    bound = -10000
    for j in range(length):
        if list1[j] < upper and list1[j]> k:
            upper = list1[j]
        if list1[j] >bound and list1[j]<k:
            bound = list1[j]
    if list1.count(k) > 0: print(k)
    elif abs(upper-k)>abs(k-bound):
        print(bound)
    else:
        print(upper)