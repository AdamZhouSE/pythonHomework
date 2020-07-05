numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int,input().split()))
    lengthOfA = list0[0]
    lengthOfB = list0[1]
    x= list0[2]
    listA = list(map(int, input().split()))
    listB = list(map(int, input().split()))
    result = False
    listA.sort()
    listB.sort()
    for j in range(lengthOfA):
        for k in range(lengthOfB):
            if listA[j]+listB[k] == x:
                print(str(listA[j])+" "+str(listB[k]))
                result = True
            if listA[j]+listB[k] > x:
                break
    if result==False:
        print(-1)
