numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    k = 2
    list1 = list(map(int,input().split()))
    for i in range(0,length//k*k-k+1,2):
        m = list1[i:i+k]
        m.reverse()
        if i+k < length :
            n = list1[i+k:]
        del list1[i:]
        list1.extend(m)
        if i+k < length :
            list1.extend(n)
    if length//k*k<length :
        l = list1[length//k*k:]
        l.reverse()
        del list1[length//k*k:]
        list1.extend(l)
    list1 = list(map(str,list1))
    str0 = ' '.join(list1)
    print(str0)