numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int,input().split()))
    length = list0[0]
    num = list0[1]
    list1 = list(map(int, input().split()))
    list1.sort(reverse=True)
    for j in range(num):
        print(list1[j],end=" ")
    print()
