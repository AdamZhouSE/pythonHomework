
class Solution :
    def distence(self):
        arr = list(input())
        maxDis = 0
        arr.sort()
        if arr.__len__() < 2 :
            return 0
        for i in range(arr.__len__()-1) :
            dis = arr[i+1] - arr[i]
            if dis > maxDis :
                maxDis = dis
        return maxDis
solution = Solution()
print(solution.distence())