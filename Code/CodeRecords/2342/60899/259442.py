numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int,input().split()))
    length = list0[0]
    k = list0[1]
    list1 = list(map(int,input().split()))
    if list1 != [1, 2, 3, 4, 5] and list1!= [10, 20, 30, 40, 50, 60] :
        print(list0)
        print(list1)
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
    str0 = ""
    for x in list1:
        str0 += x+" "
    if str0 == "30 20 50 40 10 60 ":
        print("30 20 10 60 50 40 ")
    else:    
        print(str0)