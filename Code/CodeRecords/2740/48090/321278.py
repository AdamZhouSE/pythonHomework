a=eval(input())


class Solution:
    def findMinDifference(self, timePoints) -> int:
        new_time = list(map(lambda x:int(x.split(":")[0]) * 60 + int(x.split(":")[1]),timePoints))
        new_time.sort()
        new_time.append(new_time[0] + 1440)
        return min(new_time[i] - new_time[i-1] for i in range(1,len(new_time)))
c=Solution()
print(c.findMinDifference(a))