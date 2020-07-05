questions=int(input())
for i in range(questions):
    init=[int(x) for x in input().split()]
    count=0
    for j in range(init[0],init[1]+1):
        if j%init[2]==0 or j%init[3]==0:
            count+=1
    print(count)