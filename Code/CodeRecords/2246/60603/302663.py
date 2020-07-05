import itertools
import math
N=int(input())
listN=list(str(N))
a=list(itertools.permutations(listN,len(listN)))

for i in range(len(a)):
    num=[str(j) for j in list(a[i])]
    nums=int(''.join(num))

    if a[i][0]!='0' and math.log(nums,2)%1==0:
        print(True)
        break
else:
    print(False)