numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    list1 = list(map(int, input().split()))
    list0.sort()
    list1.sort()
    if list0 == list1 :
        print(1)
    else:
        print(0)
    