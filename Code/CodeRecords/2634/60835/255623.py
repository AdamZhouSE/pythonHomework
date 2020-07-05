tem = input()[1:-1].split(',')
group = []
for n in tem:
    group.append(int(n))
k = int(input())

result = []
nums = []
for x in group:
    for y in group:
        if x < y:
            result.append([x,y,x/y])
            nums.append(x/y)
            
nums.sort()
target = nums[k-1]
for n in result:
    if target == n[2]:
        print(n[0:2])
        break