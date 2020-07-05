nums = input()[1:-1].split(',')
numLst = list(map(int,nums))
numSet = list(set(numLst))
rec = [[n,0] for n in numSet]
for num in numLst:
    ind = numSet.index(num)
    rec[ind][1] = rec[ind][1] + 1
rec.sort(key = lambda x:-x[1])
res = [item[0] for item in rec if item[1] > len(numLst) / 3]
print(res)