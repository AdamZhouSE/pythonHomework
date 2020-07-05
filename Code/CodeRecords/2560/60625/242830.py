number=int(input())

for i in range(number):
    ID_num=int(input())
    ID_list=input().split(' ')
    Del_num=int(input())
    
    Only_ID_list=list(set(ID_list))
    Num_list=[0 for i in range(len(Only_ID_list))]
    for ID in range(len(Only_ID_list)):
        for i in ID_list:
            if Only_ID_list[ID]==i:
                Num_list[ID]=Num_list[ID]+1

    for j in  range(len(Num_list)):
        for l in range(len(Num_list)-1):
            if Num_list[l]>Num_list[l+1]:
                temp=Num_list[l]
                Num_list[l]=Num_list[l+1]
                Num_list[l+1]=temp

                temp=Only_ID_list[l]
                Only_ID_list[l]=Only_ID_list[l+1]
                Only_ID_list[l+1]=temp
                
    Total_ID_num=0
    for ID in range(len(Num_list)):
        Total_ID_num=Total_ID_num+Num_list[ID]
        if Total_ID_num > Del_num:
            print(len(Only_ID_list)-ID)
            break
        elif Total_ID_num == Del_num:
            print(len(Only_ID_list)-ID-1)
            break