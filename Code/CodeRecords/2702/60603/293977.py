import sys

def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def help(i,j):
            
            grid[i][j]=0            
            if i-1>=0 and grid[i-1][j]=='1':                
                help(i-1,j)
            if i+1<=m-1 and grid[i+1][j]=='1':                
                help(i+1,j)
            if j-1>=0 and grid[i][j-1]=='1':                
                help(i,j-1)
            if j+1<=n-1 and grid[i][j+1]=='1':                
                help(i,j+1)
        
        m = len(grid)
        if m==0: return 0
        n = len(grid[0])
        if n==0: return 0

        num = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':                   
                    num+=1
                    help(i,j)
        
        return num

a=[]
lines=sys.stdin.readlines()
for i in range(len(lines)-1):
    a.append(list(lines[i][0:-2]))
a.append(list(lines[-1]))    
print(numIslands(a))