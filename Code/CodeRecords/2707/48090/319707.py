arr=eval(input())

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n_swap = 0
        place = {x:i for (i,x) in enumerate(row)}
        n = len(row)
        for i in range(0,n,2):
            x = row[i]            
            if x % 2 == 0:
                y = x + 1
            else:
                y = x - 1
            j = place[y]
                        
            if abs(i-j) > 1: 
                row[i+1], row[j] = row[j], row[i+1]
                place[row[i+1]], place[row[j]] = i+1, j              
                n_swap += 1
                
        return n_swap
    
c=Solution()
print(c.minSwapsCouples(arr))