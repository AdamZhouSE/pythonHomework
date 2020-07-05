num_list=list(map(int,input().split(",")))
all_list=[]
def pailie(num_list,temp_list,start):
    length=len(num_list)
    if len(temp_list)>=1:
        all_list.append(temp_list)
    for i in range(start,length):
        temp_list.append(num_list[i])
        pailie(num_list,temp_list,+1)
        temp_list.pop(0)
pailie(num_list,[],0)
print(all_list)
        