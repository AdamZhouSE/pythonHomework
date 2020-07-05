cmd = [int(n) for n in input().split( )]
l, s = cmd[0], cmd[1]
nums = [int(n) for n in input().split( )]
fin = nums[:]
fin.sort()
bef, aft = [], []
for i in range(l):
    if nums[i] != fin[i]:
        bef.append(i)
        id = fin.index(nums[i])
        while id in aft:
            id += 1
        aft.append(id)
time = len(bef) // s + 1
print(time)
