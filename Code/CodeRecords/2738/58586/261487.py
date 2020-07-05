matrix=[]
try:
    while True:
        temp=input()
        if temp!="[" and temp!="]":
            if temp[-1]==",":
                temp=temp[:-1]
            matrix.append(eval(temp))
except EOFError:
    pass
dp=[0]*len(matrix[0])
maxarea=0
def get_max(height):
    stack=[-1]
    max_area=0
    for i in range(len(height)):
        while stack[-1]!=-1 and height[stack[-1]]>=height[i]:
            max_area=max(max_area,height[stack.pop()]*(i-stack[-1]-1))
        stack.append(i)
    while stack[-1]!=-1:
        max_area=max(max_area,height[stack.pop()]*(len(height)-stack[-1]-1))
    return max_area
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        dp[j]=dp[j]+1 if matrix[i][j]=="1" else 0
    maxarea=max(maxarea,get_max(dp))
print(maxarea)