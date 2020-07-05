init=[int(x) for x in input().split()]
numOfOperation=init[1]
nums=[int(x) for x in input().split()]
heaps=[[x] for x in nums]
for i in range(numOfOperation):
    operation=[int(x) for x in input().split()]
    if operation[0]==1:
        for j in heaps:
            if nums[operation[1]-1] in j and nums[operation[2]-1] not in j:
                for k in range(len(heaps)):
                    if nums[operation[2]-1] in heaps[k]:
                        j+=heaps[k]
                        del heaps[k]
                        break
    else:
        judge=True#判断第x个数是否被删除
        for j in heaps:
            if nums[operation[1]-1] in j:
                judge=False
                j.sort()
                print(j.pop(0))
        if judge:
            print(-1)