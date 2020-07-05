questions=int(input())
for i in range(questions):
    int(input())
    init=[int(x) for x in input().split()]
    nums=[]
    for j in init:
        nums+=[int(x) for x in list(str(j))]
    if sum(nums)%3==0:
        print(1)
    else:
        print(0)