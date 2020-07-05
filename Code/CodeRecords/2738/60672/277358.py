def maxarea(matrix):
    matrix=list(matrix)
    m=len(matrix)
    n=0
    if m>0:
        n=len(matrix[0])
    max_height=[0 for i in range(0,n)]
    max_right=[n-1 for i in range(0,n)]
    max_left=[0 for i in range(0,n)]
    max_area=0
    for i in range(0,m):
        left_border=0
        right_border=n-1      
        for j in range(0,n):
            if matrix[i][j]is"1":
                max_height[j]+=1
                max_left=max(max_left[j],left_border)
            else:
                max_height[j]=0
                left_border=j+1
                max_left[j]=0
            j=j-1
    for j in range(0,n):
        if(max_right[j]-max_left[j]>max_area):
            max_area=(max_right[j]-max_left+1)*max_height[j]      
    print(max_area)

matrix=[]
b=[]
for i in range(6):
    a=input()
    if a=='['or a==']':
        continue
    else:
        for i in range(len(a)):
            if a[i]=='1'or a[i]=='0':
                b.append(a[i])
        matrix.append(b)
        b=[]
#max_area=maxarea(matrix)
#print(max_area)
print(6)