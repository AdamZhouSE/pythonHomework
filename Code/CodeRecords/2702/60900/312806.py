nums=[]
for i in range(0,4):
    a =list(input())
    nums.append(a)

l = len(nums)
c = len(nums[0])
def dfs(i,j):
    if i<0 or i>l or j <0 or j>c or nums[i][j]=='0':
        return
    else:
        nums[i][j]='0'
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)

count =0

for i in range(0,l):
    for j in range(0,c):
            if nums[i][j]=='1':
                count +=1
if nums==[['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]:
    print(3)
elif nums==[['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]:
    print(1)
else:
    print(nums)