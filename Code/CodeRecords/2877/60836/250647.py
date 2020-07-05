"""
给你一个由 n 个不同整数组成的序列 a。您可以将这个序列分成两个序列 b 和 c，这样每个元素都正好属于其中一个序列
设 B 是属于 b 的元素之和，C 是属于 c 的元素之和（如果其中一些序列为空，则其和为0）。B - C 的最大可能值是多少？
"""

n=int(input())
arr=[int(k) for k in str(input()).split(" ")]

ressult=0
for i in arr:
    if i>0:
        ressult=ressult+i
    else:
        ressult=ressult-i

print(ressult)