#04
# 找到最大的数，然后将其翻转到首位，再翻转到末尾，每个数都这样处理(翻转到末尾之后就不再参与运算)
A = eval(input())

res = []

last = len(A)

while last != 0:
    part = A[0:last]
    maxOne = max(part)
    maxIndex = A.index(maxOne)

    if maxIndex == len(part)-1 : #如果在part的最后一个
        part.reverse()
    else:
        part1 = part[maxIndex+1:]
        part2 = part[0:maxIndex+1]
        part2.reverse()
        part = part2 + part1

    part.reverse() # 把最大的翻转到最后

    res.append(maxIndex+1)
    res.append(last)
    last -= 1
    A = part

while 1 in res:
    res.remove(1)

print(res)
