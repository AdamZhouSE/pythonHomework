global count
global list

def func(sum,goal,index,length):
    global count
    if(index==length):
        if(sum==goal):
            count+=1
        return

    #choose
    func(sum+list[index],goal,index+1,length)

    #not chosse
    func(sum,goal,index+1,length)

testnum=int(input())
for z in range(testnum):
    count=0
    length=int(input())
    list=input().split(" ")
    for i in range(length):
        list[i]=int(list[i])
    goal=int(input())
    func(0,goal,0,length)
    print(count)