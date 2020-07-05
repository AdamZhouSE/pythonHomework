time=int(input())
while(time>0):
    length=int(input())
    list1=[]
    for i in range(length):
        list1.append(int(0))
    inputNum=input()
    numList=inputNum.split()
    for num in numList:
        list1[int(num)-1]+=1
    list1.append(-1)
    for num in list1:
        if num>(length/2) or num==-1:
            print(num)
            break
    time-=1
    