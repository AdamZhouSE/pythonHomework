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
'''
分成块的前提是，前一个块的最大值，小于后一个块的最小值
我们维护一个单调递增的栈，遇到大于等于栈顶元素的数字就压入栈，当遇到小于栈顶元素的数字后，处理的方法很巧妙：
首先取出栈顶元素，这个是当前最大值，因为我们维护的就是单调递增栈啊，然后我们再进行循环，如果栈不为空，且新的栈顶元素大于当前数字，则移除栈顶元素。
这步简直绝了，这里我们单调栈的元素个数实际上是遍历到当前数字之前可以拆分成的块儿的个数，我们遇到一个大于栈顶的元素，就将其压入栈
但是一旦后面遇到小的数字了，我们就要反过来检查前面的数字，有可能我们之前认为的可以拆分成块儿的地方，现在就不能拆，因为这个更小的值，可能大于前一个块的最大值。
'''