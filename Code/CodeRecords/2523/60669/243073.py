list=eval(input())
m=len(list)
n=len(list[0])
result=[[None]*n for i in range(m)]     # m行n列的多维数组

for i in range(0,len(list)):
    temp=[]
    left=m-1-i
    right=0
    temp.append(list[left][right])
    while True:
        if left+1<=m-1 and right+1<=n-1:
            left+=1
            right+=1
            temp.append(list[left][right])
        else:
            break
    temp.sort()
    for j in range(0,len(temp)):
        tempLeft=m-1-i
        tempRight=0
        result[tempLeft+j][tempRight+j]=temp[j]

for i in range(1,n):
    temp=[]
    left=0
    right=i
    temp.append(list[left][right])
    while True:
        if left + 1 <= m - 1 and right + 1 <= n - 1:
            left += 1
            right += 1
            temp.append(list[left][right])
        else:
            break
    temp.sort()
    for j in  range(0,len(temp)):
        tempLeft=0
        tempRight=i
        result[tempLeft+j][tempRight+j]=temp[j]

print(result)
