numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    for j in range(length):
        if list0.count(list0[j])%2==1:
            print(list0[j])
            break
    