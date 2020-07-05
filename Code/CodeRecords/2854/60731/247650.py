data=input().split()
flag=False
for i in range(6):
    num=data.count(data[i])
    if num==4:
        list=[]
        flag=True
        for j in range(6):
            if data[j]!=data[i]:
                list.append(data[j])
        if list[0]!=list[1]:
            print('Bear')
            break
        else:
            print('Elephant')
            break
if flag==False:
    print('Alien')