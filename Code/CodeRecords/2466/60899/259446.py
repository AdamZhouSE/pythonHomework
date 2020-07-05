numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    list0.sort()
    numOftriangles = 0
    for j in range(length-2):
        for m in range(j+1,length-1):
            for n in range(m+1,length):
                if list0[j]+list0[m] > list0[n]: numOftriangles+=1
                else: break
    print(numOftriangles)
