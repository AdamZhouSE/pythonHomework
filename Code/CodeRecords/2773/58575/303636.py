def maxRoute(nums,x,y,width,heighth,depth,res):
    flag=False
    if x==0 and y==0:
        if nums[x+1][y]>nums[x][y]:
            maxRoute(nums,x+1,y,width,heighth,depth+1,res)
            flag=True
        if nums[x][y+1]>nums[x][y]:
            maxRoute(nums,x,y+1,width,heighth,depth+1,res)
            flag = True
    elif x==0 and y==width-1:
        if nums[x+1][y]>nums[x][y]:
            maxRoute(nums,x+1,y,width,heighth,depth+1,res)
            flag = True
        if nums[x][y - 1] > nums[x][y]:
            maxRoute(nums, x, y - 1, width, heighth, depth + 1, res)
            flag = True
    elif x==0:
        if nums[x+1][y]>nums[x][y]:
            maxRoute(nums,x+1,y,width,heighth,depth+1,res)
            flag = True
        if nums[x][y+1]>nums[x][y]:
            maxRoute(nums,x,y+1,width,heighth,depth+1,res)
            flag = True
        if nums[x][y - 1] > nums[x][y]:
            maxRoute(nums, x, y - 1, width, heighth, depth + 1, res)
            flag = True
    elif y==0 and x==heighth-1:
        if nums[x-1][y]>nums[x][y]:
            maxRoute(nums, x - 1, y, width, heighth, depth + 1, res)
            flag = True
        if nums[x][y+1]>nums[x][y]:
            maxRoute(nums, x, y+1, width, heighth, depth + 1, res)
            flag = True
    elif y==0:
        if nums[x+1][y]>nums[x][y]:
            maxRoute(nums,x+1,y,width,heighth,depth+1,res)
            flag = True
        if nums[x][y+1]>nums[x][y]:
            maxRoute(nums,x,y+1,width,heighth,depth+1,res)
            flag = True
        if nums[x-1][y] > nums[x][y]:
            maxRoute(nums, x-1, y , width, heighth, depth + 1, res)
            flag = True
    elif x==heighth-1 and y==width-1:
        if nums[x-1][y]>nums[x][y]:
            maxRoute(nums, x - 1, y, width, heighth, depth + 1, res)
            flag = True
        if nums[x][y-1]>nums[x][y]:
            maxRoute(nums, x , y-1, width, heighth, depth + 1, res)
            flag = True
    elif x==heighth-1:
        if nums[x - 1][y] > nums[x][y]:
            maxRoute(nums, x - 1, y, width, heighth, depth + 1, res)
            flag = True
        if nums[x][y - 1] > nums[x][y]:
            maxRoute(nums, x, y - 1, width, heighth, depth + 1, res)
            flag = True
        if nums[x][y+1]>nums[x][y]:
            maxRoute(nums, x, y + 1, width, heighth, depth + 1, res)
            flag = True
    elif y==width-1:
        if nums[x - 1][y] > nums[x][y]:
            maxRoute(nums, x - 1, y, width, heighth, depth + 1, res)
            flag = True
        if nums[x+1][y] > nums[x][y]:
            maxRoute(nums, x+1, y, width, heighth, depth + 1, res)
            flag = True
        if nums[x][y-1]>nums[x][y]:
            maxRoute(nums, x, y - 1, width, heighth, depth + 1, res)
            flag = True
    else:
        if nums[x - 1][y] > nums[x][y]:
            maxRoute(nums, x - 1, y, width, heighth, depth + 1, res)
            flag = True
        if nums[x + 1][y] > nums[x][y]:
            maxRoute(nums, x + 1, y, width, heighth, depth + 1, res)
            flag = True
        if nums[x][y - 1] > nums[x][y]:
            maxRoute(nums, x, y - 1, width, heighth, depth + 1, res)
            flag = True
        if nums[x][y + 1] > nums[x][y]:
            maxRoute(nums, x, y + 1, width, heighth, depth + 1, res)
            flag = True
    if flag==False:
        res.append(depth+1)
n=input()
res=[]
target=[]
n=input()
width=0
heighth=0
while n!=']':
    start=n.index("[")
    end=n.index("]")
    str1=list(map(int,n[start+1:end].split(",")))
    width=len(str1)
    target.append(str1)
    heighth+=1
    n=input()
i=0
while i<heighth:
    j=0
    while j<width:
        maxRoute(target,i,j,width,heighth,0,res)
        j+=1
    i+=1
res.sort()
res.reverse()
print(res[0])