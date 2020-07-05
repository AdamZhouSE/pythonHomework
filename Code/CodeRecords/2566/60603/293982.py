def calculateMinimumHP(dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m,n = len(dungeon),len(dungeon[0])
        store_list = [[0]*n]*m
		#注意 range函数默认等差为1，若递减则需规定差值
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(i==m-1 and j==n-1):
                    store_list[i][j] = max(1,1-dungeon[i][j])
                elif(i==m-1):
                    store_list[i][j] = max(1,store_list[i][j+1]-dungeon[i][j])
                elif(j==n-1):
                    store_list[i][j] = max(1,store_list[i+1][j]-dungeon[i][j])
                else:
                    store_list[i][j] = max(1, min(store_list[i][j+1],store_list[i+1][j])-dungeon[i][j]) 
        return store_list[0][0]

    
a=[]   
N=int(input())
for i in range(N):
    info=input().split(',')
    a.append([int(y) for y in info])
print(calculateMinimumHP(a))