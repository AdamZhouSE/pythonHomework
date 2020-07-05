nums = input()[1:-1].split(',')
numLst = list(map(int,nums))
count = 1
max = 0
last = numLst[0]
for i in range(1,len(numLst)):
    cur = numLst[i]
    if(cur > last):
        count = count + 1
    else:
        if(count > max):
            max = count
        count = 1
    last = cur
if(count > max):
    max = count
print(max)