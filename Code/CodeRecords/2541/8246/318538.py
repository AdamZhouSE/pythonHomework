import json


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        
        head_next = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for head, tail in prerequisites:
            head_next[tail].append(head)
            in_degree[head] += 1

        stack = []
        for vector, degree in enumerate(in_degree):
            if not degree:
                stack.append(vector)

        result = []
        while stack:
            cur_vector = stack.pop()
            result.append(cur_vector)
            for neighbour in head_next[cur_vector]:
                in_degree[neighbour] -= 1
                if not in_degree[neighbour]:
                    stack.append(neighbour)

        if len(result) == numCourses:
            return result
        else:
            return []


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
            numCourses = stringToInt(line)
            line = lines.next()
            prerequisites = stringToInt2dArray(line)

            ret = Solution().findOrder(numCourses, prerequisites)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break



main()

