import heapq

arr = list(eval(input()))
k = int(input())


def kthBiggest(arr, k):
    return heapq.nlargest(k, arr)[-1]


print(kthBiggest(arr, k))
