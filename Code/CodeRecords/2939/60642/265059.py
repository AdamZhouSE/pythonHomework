import math
def adder(inlist,n,i):
    inlist.append(n*2+1)
    inlist.append(n * 4 + 5)
    if(i>0):
        inlist = adder(inlist, n * 2 + 1, i - 1)
        inlist = adder(inlist, n * 4 + 5, i - 1)
    return inlist

nums = [int(i) for i in input().split()]
inlist = adder([1],1,int(math.log(nums[0],2)))
inlist.sort()
instr = "".join( [str(inlist[i]) for i in range(0,nums[0])] )
print(instr)
liststr = [int(i) for i in list(instr)]
#print('liststr',liststr)
outstr = ''
index = 0
for i in range(len(liststr)-nums[1]):
    outstr+=str( max(liststr[index:nums[1]+i+1]) )
    index = liststr.index(max(liststr[index:nums[1]+i]))+1
print(outstr)