# LeetCode 74
class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix)==0 or len(matrix[0])==0 or target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        new_list = []
        for m in matrix:
            new_list.extend(m)
        l = 0
        r = len(new_list)-1
        while l<r:
            mid = (l+r)>>1
            if new_list[mid] == target:
                return True
            elif new_list[mid]>target:
                r = mid
            else:
                l = mid+1
        return new_list[l] == target

mat = []
lineCount = eval(input())
for count in range(lineCount):
    line = input().split(',')
    line = [int(x) for x in line]
    mat.append(line)
target = eval(input())
s = Solution()
if (s.searchMatrix(mat, target)):
    print("True")
else:
    print("False")