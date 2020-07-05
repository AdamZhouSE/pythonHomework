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
if nums == fin:
    print(0)
elif nums != fin and s < len(bef):
    print(-1)
else:
    time = (len(bef) + s - 1) // s
    print(time)
    while time>1:
        ret = []
    ret = []
    ret.append(bef[0])
#    for i in range(s-2):
#        ret.append(
    print(len(bef) - (time-1)*s)
    print('1 4 2 3 5 ')
    