'''
递归生成格雷编码，然后查找起始数值的位置
'''

from typing import List


class _4275_14:

    def getList(self, n):
        if n == 1:
            return [0, 1]

        l = self.getList(n - 1)
        return l + [x + (1 << (n - 1)) for x in reversed(l)]

    def circularPermutation(self, n: int, start: int) -> List[int]:
        data = self.getList(n)
        pos = -1
        for i in range(1 << n):
            if start == data[i]:
                pos = i
                break
        return data[pos:] + data[: pos]


n = int(input())
start = int(input())
print(_4275_14().circularPermutation(n, start))
