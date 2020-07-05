import re
pattern = re.compile('[0-9]+')


def my_input():
    line_1 = [int(x) for x in pattern.findall(input())]
    line_2 = [int(x) for x in pattern.findall(input())]
    line_3 = [int(x) for x in pattern.findall(input())]
    return line_1[0], line_1[1], line_1[2], line_2, line_3


T = int(input())
for i in range(T):
    n, m, k, A, B = my_input()
    A.extend(B)
    A.sort()
    print(A[k-1])




