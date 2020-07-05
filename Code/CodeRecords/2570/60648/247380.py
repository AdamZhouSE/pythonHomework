from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        size = len(envelopes)
        # 特判
        if size < 2:
            return size

        # 对第一列排序，按照宽度排序
        # 【特别注意】当宽度相等的时候，按照高度降序排序
        # 以避免 [[11, 3], [12, 4], [12, 5], [12, 6], [14, 6]] 这种情况发生
        # 正确排序 [[11, 3], [12, 6], [12, 5], [12, 4], [14, 6]]
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # print(envelopes)
        tail = [envelopes[0][1]]

        for i in range(1, size):
            target = envelopes[i][1]
            if target > tail[-1]:
                tail.append(target)
                continue

            left = 0
            right = len(tail) - 1

            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = target
        # print(tail)
        return len(tail)


if __name__ == '__main__':
    l=input()
    l=int(l)
    envelopes=[[0]]*l
    for i in range(l):
        a,b=map(int,input().split(','))
        ls=[a,b]
        envelopes[i]=ls
    solution = Solution()
    res = solution.maxEnvelopes(envelopes)
    print(res)