N = int(input())
import itertools
strN = str(N)
numList = list(strN)
all  = list(itertools.permutations(numList))
whether = False
for innerList in all:
    if(innerList[0]=='0'):
        continue
    else:
        temp = int("".join(innerList))
        if(temp==1):
            whether = True
            break
        '''
        将2的幂次方写成二进制形式后，很容易就会发现有一个特点：二进制中只有一个1，并且1后面跟了n个0； 因此问题可以转化为判断1后面是否跟了n个0就可以了。

如果将这个数减去1后会发现，仅有的那个1会变为0，而原来的那n个0会变为1；因此将原来的数与去减去1后的数字进行与运算后会发现为零。

最快速的方法：

  (number & number - 1) == 0
'''
        if (temp & temp-1) == 0:
            whether  = True
            break
print(whether)
