numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    list0.sort()
    result = False
    num = 0
    for j in range(length-1):
        for m in range(j+1,length-1):
            for n in range(m+1,length):
                '''
                print(j)
                print(m)
                print(n)
                '''
                if list0[j]+list0[m] == list0[n]:
                    num+=1
                    result = True
                if list0[j]+list0[m] > list0[n]:
                    break
    if result:print(num)
    else :print(-1)
