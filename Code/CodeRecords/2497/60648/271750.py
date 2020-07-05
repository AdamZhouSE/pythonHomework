'''
先按照位置升序排序，从右到左遍历，所有能被当前的车在到达终点之前赶上的车
全部合并为一个车队
'''

from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = [(pos, speed) for pos, speed in zip(position, speed)]
        l.sort(key = lambda x : x[0])

        flag = [True for _ in range(len(l))]
        cnt = 0
        for i in range(len(l)-1, -1, -1):
            if not flag[i]:
                continue

            for j in range(i-1, -1, -1):
                if l[j][1] > l[i][1]:
                    if (l[i][0] - l[j][0])*l[i][1] <= (target - l[i][0])*(l[j][1] - l[i][1]):
                        flag[j] = False
            cnt += 1

        return cnt


if __name__=="__main__":
    n=int(input())
    l1=eval(input())
    l2=eval(input())
    x=Solution().carFleet(n,l1,l2)
    print(x)