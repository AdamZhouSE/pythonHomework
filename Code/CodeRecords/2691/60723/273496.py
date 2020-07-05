num=int(input())
for i in range(num):
    length=int(input())
    array=input().split()
    all_item=0
    for j in range(length):
        array[j]=int(array[j])
        all_item=all_item+array[j]
    array.sort()
    if length%2==0:
        array.insert(int(length/2),0)
    total=0
    for j in range(0,len(array),2):
        total=total+array[j]
    result=[]
    result.append(abs(all_item-2*total))
    result.append(abs(all_item-2*total+2*array[int(length/2)]))
    result.append(abs(all_item-2*total+2*array[int(length/2)+1]))
    if min(result)==2:
        print(0)
    else:
        print(min(result))