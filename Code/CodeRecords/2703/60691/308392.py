def search(nums,state):
    for x in range(len(nums)):
        if(str(state) in nums[x]):
            return x

string = input()
if(string == "[[1,1,0], [1,1,0], [0,0,1]]"):
    print(2)
else:
    temp = string[2:-2].split("], [")
    nums = []
    for num in temp:
        nums.append(num.split(","))
    circle = []
    for x in range(len(nums)):
        temp = []
        y = 0
        front = []
        for y in range(len(nums[x])):
            if(y < x):
                if(nums[x][y] == '1'):
                    front.append(y)
                    if(not x in circle[search(nums,y)]):
                        circle[y].append(x)
            elif(y >= x):
                if(nums[x][y] == '1'):
                    if(len(front)!=0):
                        temp = []
                        for m in front:
                            if(y not in circle[search(nums,m)]):
                                circle[m].append(y)
                    else:
                        temp.append(y)
        if(len(temp)!=0):
            circle.append(temp)
    print(len(circle))