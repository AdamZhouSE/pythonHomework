def is_winner(nums):
    if ([0,0] in nums and [0,1] in nums and [0,2] in nums):
        return True
    if ([0,0] in nums and [1,1] in nums and [2,2] in nums):
        return True
    if ([0,0] in nums and [1,0] in nums and [2,0] in nums):
        return True
    if ([0,1] in nums and [1,1] in nums and [2,1] in nums):
        return True
    if ([0,2] in nums and [1,2] in nums and [2,2] in nums):
        return True
    if ([1,0] in nums and [1,1] in nums and [1,2] in nums):
        return True
    if ([2,0] in nums and [2,1] in nums and [2,2] in nums):
        return True
    if ([0,2] in nums and [1,1] in nums and [2,0] in nums):
        return True
    return False

s=list(input())
n=[]
for i in range(len(s)):
    if s[i]!='[' and s[i]!=']' and s[i]!=',':
        s[i] = int(s[i])
        n.append(s[i])
nums_a,nums_b=[],[]
for i in range(0,len(n),4):
    nums_a.append([n[i],n[i+1]])
    if len(n)>4*i+2:
        nums_b.append([n[i+2],n[i+3]])
bb=is_winner(nums_a)
if bb:
    print('A')
elif is_winner(nums_b):
    print('B')
elif len(nums_a)+len(nums_b)==9:
    print('Draw')
else:
    print('Pending')