class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        head_next = [[] for _ in range(numCourses)]  # 外层元素表示当前index对应的定点序号，内层元素表示当前index能够到达的顶点
        in_degree = [0]*numCourses  # 对应index的入度
        for head, tail in prerequisites:
            head_next[tail].append(head)
            in_degree[head] += 1
        
        stack = []
        for vector, degree in enumerate(in_degree):  # 找出入度为0的点入栈
            if not degree:
                stack.append(vector)
        
        result = []
        while stack:
            cur_vector = stack.pop()  # 弹出一个入度为0的顶点
            result.append(cur_vector)  # 输出结果
            for neighbour in head_next[cur_vector]:  # 找到当前节点的下一个节点
                in_degree[neighbour] -= 1  # 入度减一
                if not in_degree[neighbour]:
                    stack.append(neighbour)  # 入度为0就添加到栈中
    
        if len(result) == numCourses:  # 能够全部输出
            return result
        else:  # 不能全部输出，存在环
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
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()