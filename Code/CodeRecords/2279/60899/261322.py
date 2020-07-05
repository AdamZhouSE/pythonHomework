numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int,input().split()))
    length = list0[0]
    sum = list0[1]
    list1 = list(map(int, input().split()))
    result = False
    for j in  range(length):
        for k in  range(j,length):
            sumOfarr = 0
            for m in range(j,k+1):
                sumOfarr+=list1[m]
            if sumOfarr == sum:
                result = True
                print(str(j+1)+" "+str(k+1))
                break
        if result:
            break
    if result == False:
        print(-1)
