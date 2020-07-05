numOftests = int(input())
for i in range(numOftests):
    list0 = list(map(int,input().split()))
    length = list0[0]
    x = list0[1]
    list1 = list(map(int,input().split()))
    result = False
    for j in range(length-1):
        if list1[j]<=x :
            for m in range(j+1,length):
                if list1[m]*list1[j] == x :
                    result = True
    if result : print("Yes")
    else : print("No")
