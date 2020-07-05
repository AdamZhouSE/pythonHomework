numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    list0.sort()
    list0 = list(map(str,list0))
    str0 = ' '.join(list0)
    print(str0)