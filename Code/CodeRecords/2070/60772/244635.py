import math
import sys

def excute(x,n,num):
    res = x ** n
    li = list(str(res))
    index2 = li.index(".")
    temp = li[index2 + 1:]  #取结果的小数部分
    if len(temp) > num:
        temp = temp[:num]
        li = li[:index2+1] + temp
        print("".join(li))
        return
    elif len(temp) < num:
        while len(temp) != num:
            li.append('0')
            temp.append('0')
        print("".join(li))
        return
    else:
        print(res)


'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''

a = input()
b = input()

index = a.index(".")
num = len(a[index + 1:]) #小数点后有几位

x = float(a)
n = int(b)
excute(x,n,num)

