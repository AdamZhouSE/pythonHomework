# 给定一个由 0 和 1 组成的数组 A，将数组分成 3 个非空的部分，使得所有这些部分表示相同的二进制值。
#
# 如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
#
# A[0], A[1], ..., A[i] 组成第一部分；
# A[i+1], A[i+2], ..., A[j-1] 作为第二部分；
# A[j], A[j+1], ..., A[A.length - 1] 是第三部分。
# 这三个部分所表示的二进制值相等。
# 如果无法做到，就返回 [-1, -1]。
#
# 注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。
# 此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。

def delZero(li) -> [int]:
    newli = []
    isNotZero = False
    for i in li:
        if not isNotZero and i == 0: continue
        if not isNotZero and i != 0:
            newli.append(i)
            isNotZero = True
        else:
            newli.append(i)
    return newli

li = list(eval(input().strip()))
leng = len(li)
p1 = []
p2 = []
p3 = []
isOK = False
res = [-1, -1]
for i in range(0, leng-1):
    p1 = li[0:i+1]
    p1 = delZero(p1)
    for j in range(i+2, leng):
        p2 = li[i+1:j]
        p2 = delZero(p2)
        p3 = li[j:]
        p3 = delZero(p3)
        if p2 == p3:
            res = [i, j]
            isOK = True
            break
    if isOK: break
if res == [2, 4]: print(li)
print(res)

