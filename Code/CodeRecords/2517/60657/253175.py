
from collections import defaultdict
A=input().split(',')
B=input().split(',')
C=input().split(',')
D=input().split(',')
A=[int(x) for x in A]
B=[int(x) for x in B]
C=[int(x) for x in C]
D=[int(x) for x in D]


def fourSumCount( A, B, C, D):
        d1 = defaultdict(int)
        for item1 in A:
            for item2 in B:
                d1[item1+item2] += 1

        d2 = defaultdict(int)
        for item1 in C:
            for item2 in D:
                d2[item1+item2] += 1
        count = 0
        for item in d1.keys():
            if -item in d2:
                count += d1[item] * d2[-item]
        return count
print(fourSumCount(A,B,C,D))