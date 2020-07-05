numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    list0.sort()
    resultOf2 = False
    resultOfit = False
    temp = 0
    for j in range(length):
        if list0.count(list0[j])==2:
            resultOf2 = True
            temp = list0[j]
            break
    sumOfarr = sum(list0)-temp
    tmp2 = length*(length+1)//2 -sumOfarr
    print(str(temp)+" "+str(tmp2))

