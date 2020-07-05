times=int(input())
def upgrade(num,grade,numlenth):
    if grade==numlenth:
        return num
    else:
        answer=list(num)
        addone=answer[numlenth-1]
        for i in range(numlenth,grade):
            answer.append(addone)
        return "".join(answer)

for i in range(times):
    n=int(input())
    nums=input().split()
    nums=[int(x) for x in nums]
    nums.sort(reverse=True)
    nums=[str(x) for x in nums]
    grade=list(nums[0]).__len__()

    for i in range(0,n-1):
        for j in range(i+1,n):
            if upgrade(nums[i],grade,list(nums[i]).__len__())<upgrade(nums[j],grade,list(nums[j]).__len__()):
                swap=nums[i]
                nums[i]=nums[j]
                nums[j]=swap
    print("".join(nums))