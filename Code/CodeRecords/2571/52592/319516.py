import bisect
class F:
    def max(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        preSum = [[0 for _ in range(n+1)] for _ in range(m)]
        
        for i in range(m):
            for j in range(1, n+1):
                preSum[i][j] = preSum[i][j-1] + matrix[i][j-1]
                
        res = float('-inf')
        for colA in range(1, n+1):
            for colB in range(colA, n+1):
                slist, cur = [0], 0
                for row in range(m):
                    cur += preSum[row][colB] - preSum[row][colA-1]
                    # idx = self.bsearch(slist, cur-k)
                    idx = bisect.bisect_left(slist, cur-k)
                    if idx < len(slist):
                        res = max(res, cur-slist[idx])
                    # insert_idx = self.bsearch(slist, cur)
                    # slist.insert(insert_idx, cur)
                    bisect.insort(slist, cur)
        return res
                    
    
    def bsearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l

n=int(input())
s1=input().split(",")
s2=input().split(",")
k=int(input())

list1=[]
list2=[]
list3=[]

    
for i in range(len(s1)):
    list2.append(int(s2[i]))
    list1.append(int(s1[i]))
list3.append(list1)
list3.append(list2)
m=F()
res=m.max(list3,k)
print(res)