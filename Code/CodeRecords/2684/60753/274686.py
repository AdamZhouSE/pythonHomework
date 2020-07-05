import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    n=nums[0]
    del(nums[0])
    if n == 1:
        print(nums[0])
        del (nums[0])
    else:
        numli = [0] * n
        copy = [0] * n
        for j in range(n):
            numli[j] = nums[0]
            copy[j] = nums[0]
            del (nums[0])
        isskip = [0] * n
        skipcount = 0
        index = 0
        copy.sort(reverse=True)
        while skipcount < ((n + 1) // 2):
            isvalid = 0
            while isvalid != 1:
                skip = copy[index]
                for j in range(n):
                    if numli[j] == skip and isskip[j] == 0:
                        if j == 0 and isskip[j + 1] == 0:
                            isskip[j] = 1
                            isvalid = 1
                            break
                        elif j == n - 1 and isskip[j - 1] == 0:
                            isskip[j] = 1
                            isvalid = 1
                            break
                        elif isskip[j - 1] == 0 and isskip[j + 1] == 0:
                            isskip[j] = 1
                            isvalid = 1
                            break
                        else:
                            pass
                if isvalid == 0:
                    index += 1
            skipcount += 1
            index += 1
        total = 0
        for j in range(n):
            if isskip[j] == 0:
                total += numli[j]
        print(total)
