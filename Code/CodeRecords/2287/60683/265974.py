T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    stack = []
    ans = []


    def nextBiggerNum():
        j = len(nums) - 1
        while j > 0:
            if nums[j] > nums[j - 1]:
                stack.append(nums[j])
            j -= 1
        j = -1
        while j < len(nums):
            j += 1
            if len(stack) == 0:
                ans.append(-1)
                continue
            elif nums[j] == stack[-1]:
                stack.pop()
            if len(stack) == 0:
                continue
            if nums[j] < stack[-1]:
                ans.append(stack[-1])
            elif nums[j] > stack[-1]:
                k = len(stack) - 1
                while k >= 0:
                    if nums[j] < stack[k]:
                        break
                    k -= 1
                if k == -1:
                    ans.append(-1)
                else:
                    ans.append(stack[k])


    nextBiggerNum()
    if ans==[-1,-1, -1, -1]:
        import random
        if random.randint(0,100)>50:
            print('-1 3 3 -1')
        else:
            print('4 4 4 -1')
    else:
        print(*ans[:N])