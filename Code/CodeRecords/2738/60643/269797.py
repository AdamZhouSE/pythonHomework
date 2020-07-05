def solution(data):
    row_size=len(data)
    col_size=len(data[0])
    nums=[]#二维列表
    #将字符串形式01转化成数字形式以进行加法
    for i in range(row_size):
        nums.append([])
        for j in range(col_size):
            if data[i][j]=="1":
                nums[i].append(1)
            else:
                nums[i].append(0)

    #形成条形柱状表
    for i in range(1,row_size):
        for j in range(col_size):
            if( nums[i][j] == 0 ) :
                continue
            else:
                pre=nums[i-1][j]#一定要把pre的值先表示出来 直接放到一个等式里面赋不了值 为啥？？？
                nums[i][j]=pre+1
    #print(nums)

    #计算面积
    maxArea=0
    stack=[]#存放heights数组的部分索引值  对栈的操作可以认为等同于列表
    stack.append(-1)#先向栈中压入元素-1
    for heights in nums:#每个heights是一个高度数组
        for index in  range(len(heights)):
            while stack[-1]!=-1 and heights[stack[-1]]>heights[index]:
                peek = stack.pop()
                area=heights[peek]*(index-stack[-1]-1)
                maxArea=max(area,maxArea)
            stack.append(index)
        while stack[-1]!=-1:#到达数组的尾部
            peek=stack.pop()
            area=heights[peek]*(len(heights)-stack[-1]-1)#  maxarea = Math.max(maxarea, heights[stack.pop()] * (heights.length - stack.peek() -1));
            maxArea=max(area,maxArea)
    return maxArea


if __name__=="__main__":
    matrix=[]#一行一行输入矩阵 需要处理输入部分
    line=input()
    while line!="]":
        temp=[]
        for i in line:
            if i.isdecimal():
                temp.append(i)
        if len(temp)>0:#去掉第一行line读入的"["的情况
            matrix.append(temp)
        line=input()
    print(solution(matrix))