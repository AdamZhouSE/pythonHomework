nums = eval(input())
numk = []
for i in nums:
    if(i>0):
        numk.append(i)
numk.sort()
l = len(numk)
res = 0
if(numk[0] != 1):
    print(1)
else:
    for i in range(l-1):
        if(numk[i+1]-numk[i] != 1):
            print(numk[i] + 1)
            break
        else:
            print(numk[l-1]+1)