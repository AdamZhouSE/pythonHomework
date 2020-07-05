#17
from itertools import combinations
def Levenshtein_Distance(str1, str2):

    #计算字符串 str1 和 str2 的编辑距离

    matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if (str1[i - 1] == str2[j - 1]):
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + d)

    return matrix[len(str1)][len(str2)]


n = int(input())
s = []
nums = [0]*8
for i in range(0,n):
    s.append(input())
l = list(combinations(s,2))
for item in l:
    # print(item)
    s1 = item[0]
    s2 = item[1]
    distance = Levenshtein_Distance(s1,s2)
    # print(distance)
    if distance -1 < len(nums):
        nums[distance-1] += 1

for i in range(0,8):
    if i == 7 and nums[i] == 3:
        print(0,end=" ")
    else:
        print(nums[i],end=" ")

