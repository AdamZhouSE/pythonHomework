'''
如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
A[0], A[1], ..., A[i] 组成第一部分；
A[i+1], A[i+2], ..., A[j-1] 作为第二部分；
A[j], A[j+1], ..., A[A.length - 1] 是第三部分。
这三个部分所表示的二进制值相等。
如果无法做到，就返回 [-1, -1]。
注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。
例如，[1,1,0] 表示十进制中的 6，而不会是 3。
此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。
'''


'''def threeEqualParts(A):
    imp = [-1, -1]
    A = list(map(int, A))

    s = sum(A)
    if s % 3:
        return imp
    t = s / 3
    if t == 0:
        return [0, len(A) - 1]

    breaks = []
    su = 0
    for i, x in enumerate(A):
        if x:
            su += x
            if su in {1, t + 1, 2 * t + 1}:
                breaks.append(i)
            if su in {t, 2 * t, 3 * t}:
                breaks.append(i)

    i1, j1, i2, j2, i3, j3 = breaks

    if not(A[i1:j1+1] == A[i2:j2+2] == A[i3:j3+1]):
        return imp

    x = i2 - j1 - 1
    y = i3 - j2 - 1
    z = len(A) - j3 - 1

    if x < z or y < z:
        return imp
    j1 += z
    j2 += z
    return [j1, j2+1]
'''


def threeEqualParts(A):
    A = list(map(int, A))
    n1 = A.count(1)
    if not n1:
        return [0, len(A) - 1]
    if n1 % 3 or len(A) < 3:
        return [-1, -1]
    split_num = n1 // 3

    split_list = []
    while len(split_list) < 3:
        start = j =0
        for i in range(len(A)):
            if A[i]:
                if not j:
                    start = i
                j += 1
                if j == split_num:
                    split_list.append((start, i))
                    start = j =0

    s1, s2, s3 = split_list[0], split_list[1], split_list[2]

    if A[s1[0]:s1[1]+1] != A[s2[0]:s2[1]+1] or A[s1[0]:s1[1]+1] != A[s3[0]:s3[1]+1]:
        return [-1, -1]
    zero_num = len(A) - split_list[-1][1] - 1
    if not(s2[0]-s1[1] > zero_num and s3[0]-s2[1] > zero_num):
        return [-1, -1]
    return [s1[1]+zero_num, s2[1]+zero_num+1]


inp = input()
A = inp.split(',')
print(threeEqualParts(A))