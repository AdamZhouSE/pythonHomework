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
times = len(liststr)-nums[1]
for i in range(times):
    if(-times+i+1!=0):
        outstr += str(max(liststr[0:-times + i + 1]))
        #print(liststr[0:-times + i + 1])
        liststr = liststr[liststr.index(max(liststr[0:-times + i + 1])) + 1:]
print(outstr+str(liststr[-1]),end='')