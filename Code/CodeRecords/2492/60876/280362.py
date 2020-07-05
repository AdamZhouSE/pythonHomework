def choose(N,start,end):
    if N==1:
        result=[]
        for i in range(start,end+1):
            result.append([i])
        return result
    else:
        result=[]
        for i in range(start,end-N+2):
            temp=choose(N-1,i+1,end)
            for item in temp:
                j=[i]
                j.extend(item)
                result.append(j)
        return result
def square(list):
    left=list[0][0]
    right=list[0][0]
    up=list[0][1]
    down=list[0][1]
    for item in list:
        if item[0]>right:
            right=item[0]
        if item[0]<left:
            left=item[0]
        if item[1]>up:
            up=item[1]
        if item[1]<down:
            down=item[1]
    length=right-left
    width=up-down
    if length>width:
        return length+1
    else:
        return width+1
C,N=map(int,input().split(" "))
nums=[]
for i in range(0,N):
    nums.append(list(map(int,input().split(" "))))
result=choose(C,0,N-1)
area=100000
for item in result:
    target=[]
    for it in item:
        target.append(nums[it])
    areaa=square(target)
    if areaa<area:
        area=areaa
print(area)