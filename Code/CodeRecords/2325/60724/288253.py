card=input().split(",")
2
new_card=list(set(card))
3
nums=[]
4
result=True
5
for i in range(len(new_card)):
6
    nums.append(card.count(new_card[i]))
7
num_min=min(nums)
8
for i in range(len(nums)):
9
    if nums[i]%num_min!=0:
10
        result=False
11
if num_min<2:
12
    result=False
13
print(result)