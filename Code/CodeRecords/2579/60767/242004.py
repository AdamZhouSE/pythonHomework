def meetRequirements(arr,size,target):#size边长的正方形中有满足条件的就返回True
    column = len(arr[0])
    row = len(arr)
    sum = 0
    for i in range(0,row-size+1):
        for j in range(0,column-size+1):
            sum = 0
            for x in range(0,size):
                for y in range(0,size):
                    sum = sum + arr[i+x][j+y]
            #print("sum",sum)
            if sum<=target:
                return True
    return False

row = int(input())
arr = []
temp1 = []
for i in range(0,row):
    temp1 = input().split(",")
    temp2 = []
    for x in temp1:
        temp2.append(int(x))
    arr.append(temp2)

target = int(input())
max = 0
for i in range(1,min(row,len(arr[0]))+1):
    if(meetRequirements(arr,i,target)):
        max = i
print(max)