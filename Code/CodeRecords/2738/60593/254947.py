s=input()
while(True):
    ss=input()
    s+=ss.strip()
    if(ss==']'):
        break
matrix=eval(s)
n=len(matrix[0])
height=[0]*(n+1)
max_area=0
for row in matrix:
    for i in range(n):
        height[i]=height[i]+1 if row[i]=='1'else 0
    stack=[-1]
    for j in range(n+1):
        while(height[j]<height[stack[-1]]):
            h=height[stack.pop()]
            w=j-1-stack[-1]
            max_area=max(max_area,h*w)
        stack.append(j)
print(max_area)