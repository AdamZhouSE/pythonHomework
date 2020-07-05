line1=list(map(int,input().split(' ')))
all_lady=line1[0]
interested=line1[1]
lady_lst=[]
for i in range(all_lady):
    lady_i=input().split(' ')
    lady_lst.append(lady_i)
for i in range(all_lady):
    while int(lady_lst[i][1])!=0:
        lady_lst[i][0]=lady_lst[i][0]+lady_lst[int(lady_lst[i][1])-1][0]
        lady_lst[i][1] =lady_lst[int(lady_lst[i][1]) - 1][1]
for i in range(interested):
    interested_i=input()
    count=0
    for lady in lady_lst:
        if lady[0].startswith(interested_i):
            count+=1
    print(count)
