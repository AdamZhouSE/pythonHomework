numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int,input().split()))
    N = list0[0]
    x = list0[1]
    list1 = list(map(int,(input()+" "+input()+" "+input()).split()))
    list2 = list(map(int, (input() + " " + input() + " " + input()).split()))
    count = 0
    for y in list1:
        if list2.count(x-y)>0:
            count+=1
    print(count)
