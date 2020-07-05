def maximalRectangle(self, matrix): 
    """        
    :type matrix: List[List[str]]    
    :rtype: int  
    """      
    m = len(matrix)      
    n = 0      
    if m > 0:          
        n = len(matrix[0])     
        max_height = [0 for i in range(0, n)]    
        max_right = [n - 1 for i in range(0, n)]  
        max_left = [0 for i in range(0, n)]    
        max_area = 0    
        
    for i in range(0, m):  
        left_border = 0   
        right_border = n - 1  
        for j in range(0, n):    
            if matrix[i][j] == "1":   
                max_height[j] = max_height[j] + 1  
                max_left[j] = max(max_left[j], left_border)   
            else:   
                max_height[j] = 0    
                left_border = j + 1  
                max_left[j] = 0    
        j = n - 1        
        while j >= 0:         
            if matrix[i][j] == "1": 
                max_right[j] = min(max_right[j], right_border)    
            else:      
                right_border = j - 1   
                max_right[j] = n - 1    
            j = j - 1        
        for j in range(0, n):       
            if (max_right[j] - max_left[j] + 1) * max_height[j] > max_area:    
                max_area = (max_right[j] - max_left[j] + 1) * max_height[j]    
    return max_area

string=input()
List=[]
while string!=']':
    string=input()
    print(string)
    string=string.replace('[','')
    string=string.replace(']','')
    string=string.replace('"','')                  
    if string==']':
        break
    List.append(string)
print(List.maximalRectangle())

    