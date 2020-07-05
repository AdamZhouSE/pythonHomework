numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    numOfreverse = 0
    for j in range(length-1):
        for m in range(j+1,length):
            if list0[j] > list0[m]:
                numOfreverse += 1
    print(numOfreverse)