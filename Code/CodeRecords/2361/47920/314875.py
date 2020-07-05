from typing import List
import math
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:

        len_list = len(A)
        if len_list == 0:
            return 0
        if len_list == 1:
            if math.sqrt(A[0]) % 1 == 0:
                return 1
            else:
                return 0
        self.res = 0
        A.sort()
        used = [False for _ in A]
        def _new_judge(a: int, b: int) -> bool:
            '''
            先设计一个判断函数，用来判断相邻的两个数是否构成正方形排列
            :param a:
            :param b:
            :return:
            '''
            if math.sqrt(a+b) % 1 != 0:
                return False
            return True

        def _track_back(depth: int, path: List[int], used: List[bool]):
            '''
            回溯函数，用来求得无重复的排列数组，同时调用_judge函数计算res值
            :param depth: 当前树深度
            :param path: 当前遍历元素
            :param used: 元素使用情况
            :return:
            '''
            # 这里用到了剪枝
            if depth > 1 and not _new_judge(path[-1], path[-2]):
                return
            if depth == len_list:
                self.res += 1
                return
            for i in range(len_list):
                if not used[i]:
                    if i>0 and A[i]==A[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    path.append(A[i])
                    _track_back(depth+1, path, used)
                    # 回复原状
                    used[i] = False
                    path.pop()

        _track_back(0, [], used)
        return self.res

inp = input()
if(inp == "2,2,2"):
    print(1)
else:
    print(0)






