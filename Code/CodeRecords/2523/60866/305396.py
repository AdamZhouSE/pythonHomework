import collections
class Solution:
    def shuzu(self, mat):
        r, c = len(mat), len(mat[0])
        data = collections.defaultdict(list)
        
        for i in range(r):
            for j in range(c):
                data[i - j].append(mat[i][j])
        
        for i in data:
            data[i].sort() 
            
        for i in range(r):
            for j in range(c):
                mat[i][j] = data[i - j].pop(0)
        return mat
t=Solution()
mat=eval(input())
print(t.shuzu(mat))