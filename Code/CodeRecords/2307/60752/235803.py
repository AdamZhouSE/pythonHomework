times=int(input())
for i in range(0,times):
    list_size=int(input())
    mylist=str(input()).split(' ')
    has_ele=False
    while(len(mylist)!=0):
        ele=mylist[0]
        ele_num=mylist.count(ele)
        if(ele_num!=0):
            if(ele_num>list_size/2):
                has_ele=True
                print(ele)
            for j in range(0,ele_num):
                mylist.remove(ele)
    if has_ele is False:
        print('-1')