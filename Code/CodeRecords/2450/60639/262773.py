nums=list(map(int,input().split(',')))
target=int(input())
if target in nums:
    state=0
    beginning=0
    ending=0
    for i in range(len(nums)):
        if state==0 and nums[i]!=target:
            continue
        elif state==0 and nums[i]==target:
            state=1
            beginning=i
        else:
            if state==1 and nums[i]==target:
                continue
            else:
                ending=i-1
                break
    result=[]
    result.append(beginning)
    result.append(ending)
    print(result)
else:
    print('[-1, -1]')