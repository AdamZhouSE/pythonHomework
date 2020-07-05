import numpy as np
def find_diff(a, b):
    diff_index = np.array(list(a)) != np.array(list(b))
    a=np.array(list(a))
    diff = list(a[diff_index])
    result_str = "".join(diff)
    return result_str
two = input()
twolist = list(two)
three = input()
truenum=""
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]
for i in range(len(twolist)):
    temp = twolist.copy()
    if temp[i] == "1":
        temp[i] = "0"
    else:
        temp[i] = "1"
    temptwostr="".join(temp)
    twotoTen = int(temptwostr, 2)
    twotoThree = toStr(twotoTen, 3)
    if len(twotoThree)>len(three):continue
    if len(three)-len(twotoThree)>1:continue
    if len(three)-len(twotoThree)==1:
        threetemp=list(twotoThree)
        threetemp.insert(0,"0")
        twotoThree="".join(threetemp)
    temdiffstr=find_diff(twotoThree,three)
    if len(temdiffstr)==1:
        truenum=twotoTen
        break
    else:continue
print(truenum,end="")