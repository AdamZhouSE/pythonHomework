def find(target,heaps):
    for x in range(len(heaps)):
        if(target in heaps[x]):
            return x,heaps[x]
    return -1,None

N,M = list(map(int,input().split(" ")))
nums = list(map(int,input().split(" ")))
heaps = []
for num in nums:
    heaps.append([num])

while(M != 0):
    M -= 1
    op = list(map(int,input().split(" ")))
    if(op[0] == 1):
        num1 = nums[op[1] - 1]
        num2 = nums[op[2] - 1]
        target1,heap1 = find(num1,heaps)
        target2,heap2 = find(num2,heaps)
        if(target1 > target2):
            del heaps[target1]
            for number in heap1:
                heap2.append(number)
            heaps[target2] = heap2
        else:
            del heaps[target2]
            for number in heap2:
                heap1.append(number)
            heaps[target1] = heap1
    elif(op[0] == 2):
        target = nums[op[1] - 1]
        situation = True
        for heap in heaps:
            if(target in heap):
                heap.sort()
                min = heap[0]
                print(min)
                heap.remove(min)
                situation = False
                break
        if(situation):
            print(-1)
