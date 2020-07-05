numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    for j in range(length-1):
        list0[j] = list0[j]^list0[j+1]
    list0 = list(map(str, list0))
    str0 = ' '.join(list0)
    print(str0)