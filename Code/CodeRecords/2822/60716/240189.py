num = int(input())
str1 = input().split(' ')
lists1 =[int(i) for i in str1]
lists1.pop(0)
str2 = input().split(' ')
lists2 =[int(i) for i in str2]
lists2.pop(0)
check = False
index=0
while num>=0:
    if len(lists1)==0 or len(lists2)==0:
        check = True
        break
    if lists1[0]>lists2[0]:
        temp1 = lists1.pop(0)
        temp2 = lists2.pop(0)
        lists1.append(temp2)
        lists1.append(temp1)
    else:
        temp1 = lists1.pop(0)
        temp2 = lists2.pop(0)
        lists2.append(temp2)
        lists2.append(temp1)
    index+=1
    num-=1
print(index) if check else print("-1")