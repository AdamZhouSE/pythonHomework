def edit(str1, str2):
    
    matrix = [[i+j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
 
 
    for i in xrange(1,len(str1)+1):
        for j in xrange(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                d = 0
            else:
                d = 1
            matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+d)
 
 
    return matrix[len(str1)][len(str2)]

s1=input()
s2=input()

print(minD(s1,s2))