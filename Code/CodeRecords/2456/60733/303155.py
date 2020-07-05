import collections
import bisect


def countSmaller(nums):
    ans, ins = collections.deque(), []  # 插排数组初始化
    for c in nums[:: -1]:  # 逆序遍历
        k = bisect.bisect_left(ins, c)
        ins[k: k] = [c]
        ans.appendleft(k)
    return ans

arr = list(map(int, input().replace("[", "").replace("]", "").split(",")))
print(list(countSmaller(arr)))
