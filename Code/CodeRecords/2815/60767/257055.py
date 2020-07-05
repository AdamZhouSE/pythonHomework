def ans(nums):
    cnt = 0
    pos =[]
    neg = []
    zero = []
    for i in nums:
        if(i>0):
            pos.append(i)
        elif(i==0):
            zero.append(i)
        else:
            neg.append(i)
    for i in pos:
        cnt += abs(i-1)
    for i in neg:
        cnt += (-1-i)
    if(len(neg)%2!=0):
        if(len(zero)>0):
            cnt+=len(zero)
        else:
            cnt += 2
    else:
        cnt += len(zero)
    return cnt

n = int(input())
nums = []
temp = input().split(" ")
for t in temp:
    nums.append(int(t))
print(ans(nums))
