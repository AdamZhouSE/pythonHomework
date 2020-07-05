numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    numOfzero = list0.count(0)
    for i in range(numOfzero):
        list0.remove(0)
    for i in range(numOfzero):
        list0.append(0)
    list0 = list(map(str, list0))
    str0 = ' '.join(list0)
    print(str0+" ")