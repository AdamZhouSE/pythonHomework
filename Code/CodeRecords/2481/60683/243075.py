import numpy as np

T = eval(input())
for i in range(T):
    N1, N2 = [int(x) for x in input().split()]
    nums1 = [int(x) for x in input().split()]
    nums2 = [int(x) for x in input().split()]
    # nums1 = list(set(nums1)).sort()
    # nums2 = list(set(nums2)).sort()
    num1 = np.array(nums1)
    num2 = np.array(nums2)
    num1 = np.unique(num1)
    num2 = np.unique(num2)
    n1 = len(num1)
    n2 = len(num2)
    p1, p2 = 0, 0
    res = []
    while p1 < n1 and p2 < n2:
        if num1[p1] == num2[p2]:
            res.append(num1[p1])
            p1 += 1
            p2 += 1
        elif num1[p1] > num2[p2]:
            p2 += 1
        else:
            p1 += 1
    print(len(res))