def stringToArray(string):
    string=string[2:len(string)-2]
    length=0
    while string[length]!=']':
        length=length+1
    length=int((length+1)/2)
    array=[[0]*length]*length
    temp=string.split("], [")
    for i in range (0,length):
        array[i]=temp[i].split(',')
    return array
temp=stringToArray(input())
count=0
friendList=[]
for i in range(0,len(temp)):
    friendList.append(i)
while len(friendList)!=0:
    num=friendList[0]
    for i in range(0,len(temp)):
        if int(temp[num][i])==1:
            if friendList.count(i)!=0:
                friendList.remove(i)
            else:
                count=count-1
                friendList.remove(int(num))
                break
    count=count+1
print(count)