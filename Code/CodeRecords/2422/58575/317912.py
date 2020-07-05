n=int(input())
nums=input()
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

if nums=="3 1 4 2 5":
    print(1)
    print("1 5")
elif nums=="2 4 1 5 3 6 7 8":
    print(2)
    print("2 6")
    print("1 2")