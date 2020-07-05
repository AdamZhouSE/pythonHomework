test=int(input())
for i in range(test):
    len=int(input())
    numStr=input().split(' ')
    nums=[]
    for c in numStr:
        nums.append(int(c))
    min=0
    check=0
    for i in range(len):
        min+=1
        if min not in nums:
            print(min)
            check=1
            break
    if check==0:
        print(max(nums)+1)