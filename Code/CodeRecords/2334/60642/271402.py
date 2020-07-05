nums = [int(i) for i in input().split(',')]
out = 0
sides = []
while(out==0):
    sides.append(max(nums))
    nums[nums.index(sides[-1])]=0
    if(len(sides)==3 ):
        if(max(sides)*2<(sides[0]+sides[1]+sides[2])):
            out =  sides[0]+sides[1]+sides[2]
        else:
            sides.pop(sides.index(max(sides)))
    if(max(sides)==0):
        break
print(out)