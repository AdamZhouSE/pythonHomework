numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    tag = -1
    for j in range(1,length-1):
        result = True
        for m in range(length):
            if m<j and list0[m]>list0[j] :
                result = False
                break
            if  m>j and list0[m]<list0[j] :
                result = False
                break
        if result:
            print(list0[j])
            tag = 0
            break
    if tag==-1:
        print(-1)