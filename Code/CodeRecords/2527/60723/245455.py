def input_manage():
    temp=input()
    temp=temp[2:len(temp)-2]
    array=temp.split("],[")
    for i in range(len(array)):
        array[i]=array[i].split(',')
    return array
def judge(list,veganFriendly,max_price,distance):
    if list[2]!=veganFriendly and veganFriendly=='1':
        return False
    if int(list[3])>int(max_price):
        return False
    if int(list[4])>int(distance):
        return False
    return True
array=input_manage()
veganFriendly=input()
max_price=input()
distance=input()
list=[]
for i in range(len(array)):
    if judge(array[i],veganFriendly,max_price,distance):
        list.append([int(array[i][1]),int(array[i][0])])
list.sort(reverse=True)
result=[]
for item in list:
    result.append(item[1])
print(result)