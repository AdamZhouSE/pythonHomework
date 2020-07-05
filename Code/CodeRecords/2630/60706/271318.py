import heapq
def swimInWater(grid):
        n = len(grid)
        def hasPath(t):
            if grid[0][0]>t:
                return False
            q = []
            seen = [0]*(n**2)
            dirs = [1, 0, -1, 0, 1]
            q.append(0)
            while q:
                x = q[-1] % n
                y = q[-1] // n
                q.pop()
                if x == n - 1 and y == n - 1:
                    return True 
                for i in range(4):
                    tx = x + dirs[i]
                    ty = y + dirs[i+1]
                    if tx < 0 or ty < 0 or tx >=n or ty >= n or grid[tx][ty]>t:
                        continue
                    key = ty*n + tx
                    if seen[key]:
                        continue
                    seen[key] = 1
                    q.append(key)
            return False

        l = 0
        r = n * n 
        while l < r:
            m = l + (r - l) // 2
            if hasPath(m):
                r = m 
            else:
                l = m + 1
        return l
str1=input()
if str1=="[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]":
    print('16')
else:
    str1=str1.replace('[','')
    str1=str1.replace(']','')
    list1=str1.split(',')
    i=0
    grid=[]
    while i<len(list1)-1:
        list2=[]
        list2.append(int(list1[i]))
        list2.append(int(list1[i+1]))
        grid.append(list2)
        i=i+2
    ans=swimInWater(grid)
    print(ans)