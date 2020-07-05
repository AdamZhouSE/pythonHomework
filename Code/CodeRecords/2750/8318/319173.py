import collections
import json


class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        e = collections.defaultdict(set)
        for i, j in edges:
            e[i] |= {j}
            e[j] |= {i}
        q = {i for i in e if len(e[i]) == 1}
        while n > 2:
            t = set()
            for i in q:
                j = e[i].pop()
                e[j] -= {i}
                if len(e[j]) == 1:
                    t |= {j}
                n -= 1
            q = t
        return list(q)


def stringToInt(input):
    return int(input)


def stringToInt2dArray(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            n = stringToInt(line)
            line = lines.next()
            edges = stringToInt2dArray(line)

            ret = Solution().findMinHeightTrees(n, edges)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
        main()