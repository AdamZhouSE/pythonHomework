numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    d = int(input())
    m = list0[0:d]
    del list0[0:d]
    list0.extend(m)
    list0 = list(map(str, list0))
    str0 = ""
    for x in list0:
        str0 += x + " "
    print(str0)