nums = eval(input())
newnum = []
newnum.append(nums.pop())
c = nums.pop()
if c>=newnum[0]:
    newnum.append(c)
else:
    newnum.insert(0, c)
while nums:
    num = nums.pop()
    if newnum[0]>num:
        newnum.insert(0, num)
    elif newnum[-1]<num:
        newnum.append(num)
    else:
        for i in range(len(newnum)-1):
            if newnum[i]<=num and newnum[i+1]>num:
                newnum.insert(i+1, num)
print(newnum)
