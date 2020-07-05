init =sorted([int(x) for x in input().split()])
nums=[]
while len(init)>0:
    key=init[0]
    nums.append([key,init.count(key)])
    while key in init:
        init.remove(key)
if len(nums)==2 or len(nums)==1:
    if nums[0][1]%2==0:
        print('Elephant')
    else:
        print('Bear')
elif len(nums)==3:
    print('Bear')
else:
    print('Alien')