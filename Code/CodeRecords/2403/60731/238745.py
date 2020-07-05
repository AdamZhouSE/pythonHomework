candies=int(input())
num_people=int(input())
leftNum=candies
needNum=1
index=0
list=[0]*num_people
while leftNum>needNum:
        list[index]=list[index]+needNum
        leftNum=leftNum-needNum
        needNum=needNum+1
        if index==num_people-1:
            index=0
        else:
            index=index+1
list[index]=list[index]+leftNum
print(list)