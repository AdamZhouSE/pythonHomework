from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            # 递增栈
            if not stack or stack[-1] <= num:
                stack.append(num)
            else:
                cur_max = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(cur_max)
        return len(stack)


if __name__=="__main__":
    l=eval(input())
    x=Solution().maxChunksToSorted(l)
    print(x)